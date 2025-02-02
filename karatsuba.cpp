#include <iostream>
#include <cmath>
#include <string>

using namespace std;

long long karatsuba(long long x, long long y) {
    // xy if 10 <
    if (x < 10 || y < 10) {
        return x * y;
    }
    
    // decide
    int n = max(to_string(x).length(), to_string(y).length());
    int m = n / 2;
    
    // duvide number
    long long high_x = x / pow(10, m);
    long long low_x = x % static_cast<long long>(pow(10, m));
    long long high_y = y / pow(10, m);
    long long low_y = y % static_cast<long long>(pow(10, m));
    
    // recurtion
    long long z0 = karatsuba(low_x, low_y);        // bd
    long long z1 = karatsuba((low_x + high_x), (low_y + high_y));  // (a+b)(c+d)
    long long z2 = karatsuba(high_x, high_y);      // ac
    
    // sum
    return (z2 * pow(10, 2 * m)) + ((z1 - z2 - z0) * pow(10, m)) + z0;
}

int main() {
    long long x = 3141592653589793;
    long long y = 2718281828459045;
    
    cout << "Hasil: " << karatsuba(x, y) << endl;
    
    return 0;
}