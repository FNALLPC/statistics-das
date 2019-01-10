#include <cmath>
double dbexp(double x, double a, double b, double c)
{
  return a*exp(-x/b)/b + (1-a)*exp(-x/c)/c;
}

