//
// Created by deren zhu on 2019/9/22.
//

#ifndef C_EXTENSIONS_SAMPLE_H
#define C_EXTENSIONS_SAMPLE_H

extern int gcd(int, int);
extern int in_mandel(double x0, double y0, int n);
extern int divide(int a, int b, int* remainder);
extern double avg(double* a, int n);

typedef struct Point {
    double x, y;
} Point;

extern double distance(Point* p1, Point* p2);
#endif //C_EXTENSIONS_SAMPLE_H
