import os

import hydra
import torch
from omegaconf import DictConfig
import lightning.pytorch as pl

from fbp.model import MyModel
from fbp.data import MyDataModule


@hydra.main(config_path="conf", config_name="config", version_base="1.3")
def main(cfg: DictConfig):
    pl.seed_everything(cfg.other.seed)
    torch.set_float32_matmul_precision(cfg.model.train.matmul_precision)
    dm = MyDataModule(
        csv_path=cfg.data.data.csv_path,
        val_size=cfg.data.data.val_size,
        dataloader_num_wokers=cfg.data.data.dataloader_num_wokers,
        batch_size=cfg.data.data.batch_size,
        tokenizer_model_name=cfg.model.model.name,
        text_max_length=cfg.model.data.text_max_length,
        labels=cfg.other.labels,
    )
    model = MyModel(cfg)

    loggers = [
        pl.loggers.CSVLogger(cfg.log.artifacts.experiment_folder, name=cfg.log.artifacts.experiment_name),
        pl.loggers.MLFlowLogger(
            experiment_name=cfg.log.artifacts.experiment_name,
            tracking_uri=cfg.log.artifacts.experiment_tracking_uri,
        ),
        pl.loggers.TensorBoardLogger(
            cfg.log.artifacts.experiment_tensor_folder, name=cfg.log.artifacts.experiment_name
        ),
        pl.loggers.WandbLogger(
            project=cfg.log.artifacts.experiment_wandb_project, name=cfg.log.artifacts.experiment_name
        ),
    ]

    callbacks = [
        pl.callbacks.LearningRateMonitor(logging_interval=cfg.other.callbacks.logging_interval),
        pl.callbacks.DeviceStatsMonitor(),
        pl.callbacks.RichModelSummary(max_depth=cfg.other.callbacks.model_summary.max_depth),
    ]

    if cfg.other.callbacks.swa.use:
        callbacks.append(
            pl.other.callbacks.StochasticWeightAveraging(swa_lrs=cfg.other.callbacks.swa.lrs)
        )

    if cfg.log.artifacts.checkpoint.use:
        callbacks.append(
            pl.callbacks.ModelCheckpoint(
                dirpath=os.path.join(
                    cfg.log.artifacts.checkpoint.dirpath, cfg.log.artifacts.experiment_name
                ),
                filename=cfg.log.artifacts.checkpoint.filename,
                monitor=cfg.log.artifacts.checkpoint.monitor,
                save_top_k=cfg.log.artifacts.checkpoint.save_top_k,
                every_n_train_steps=cfg.log.artifacts.checkpoint.every_n_train_steps,
                every_n_epochs=cfg.log.artifacts.checkpoint.every_n_epochs,
            )
        )

    trainer = pl.Trainer(
        accelerator=cfg.model.train.accelerator,
        devices=cfg.model.train.devices,
        precision=cfg.model.train.precision,
        max_steps=cfg.model.train.num_warmup_steps + cfg.model.train.num_training_steps,
        accumulate_grad_batches=cfg.model.train.grad_accum_steps,
        val_check_interval=cfg.model.train.val_check_interval,
        overfit_batches=cfg.model.train.overfit_batches,
        num_sanity_val_steps=cfg.model.train.num_sanity_val_steps,
        deterministic=cfg.model.train.full_deterministic_mode,
        benchmark=cfg.model.train.benchmark,
        gradient_clip_val=cfg.model.train.gradient_clip_val,
        profiler=cfg.model.train.profiler,
        log_every_n_steps=cfg.model.train.log_every_n_steps,
        detect_anomaly=cfg.model.train.detect_anomaly,
        enable_checkpointing=cfg.log.artifacts.checkpoint.use,
        logger=loggers,
        callbacks=callbacks,
    )

    if cfg.model.train.batch_size_finder:
        tuner = pl.tuner.Tuner(trainer)
        tuner.scale_batch_size(model, datamodule=dm, mode=cfg.model.train.scaler_mode)

    trainer.fit(model, datamodule=dm)


if __name__ == "__main__":
    main()
