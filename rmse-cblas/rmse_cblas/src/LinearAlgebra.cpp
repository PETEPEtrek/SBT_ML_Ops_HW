#include "LinearAlgebra.h"
#include <cblas.h>
#include <math.h>
#include <iostream>
#include <vector>

double
LinearAlgebra::rmseBlas(const std::vector<double> &a,
                          const std::vector<double> &b) {
  size_t aLen = a.size();
  size_t bLen = b.size();

  if (aLen != bLen) {
    throw std::runtime_error("The length of the 1st vector must "
                             "equal the length of the 2nd vector");
  }

  std::vector<double> b_copy(aLen);
  cblas_dcopy(aLen, &b[0], 1, &b_copy[0], 1);

  cblas_daxpby(aLen, -1, &a[0], 1, 1, &b_copy[0], 1);
  double sum_of_squares = cblas_ddot(aLen, &b_copy[0], 1, &b_copy[0], 1);

  return sqrt(sum_of_squares / aLen);
}
