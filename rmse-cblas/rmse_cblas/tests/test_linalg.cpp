#include "LinearAlgebra.h"
#include <gtest/gtest.h>

TEST(LinearAlgebraTests, RMSEBlas) {
  std::vector<double> vector_a = {1.0, 0.0, 1.0, 0.0};
  std::vector<double> vector_b = {1.0, 0.0, 1.0, 0.0};
  auto result = LinearAlgebra::rmseBlas(vector_a, vector_b);
  EXPECT_DOUBLE_EQ(result, 0.0);
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
