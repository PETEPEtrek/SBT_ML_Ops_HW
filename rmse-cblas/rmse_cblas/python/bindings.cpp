#include "LinearAlgebra.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(linalg_core, m) {
  m.doc() = R"doc(
    Python bindings for LinearAlgebra library
  )doc";

  py::class_<LinearAlgebra>(m, "LinearAlgebra")
      .def_static("rmseBlas", &LinearAlgebra::rmseBlas, R"doc(
          RMSE using BLAS.

          Parameters:
            a : list of float
                The first vector.
            b : list of float
                The second vector.

          Returns:
            float
                The result of RMSE.
      )doc");
}
