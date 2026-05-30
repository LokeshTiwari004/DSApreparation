#include<iostream>
using namespace std;

int main()
{
    int n; cin >> n;
    for (int i=0; i < n; i++) {
        int m; cin >> m;
        for (int j=0; j < m; ++j) {
            if (j % 2) {
                cout << ((m+j) % 2 ? m+j : m+j+1) << " "; 
            } else {
                cout << j+1 << " ";
            }
        }
        cout << "\n";
    }
    return 0;
}