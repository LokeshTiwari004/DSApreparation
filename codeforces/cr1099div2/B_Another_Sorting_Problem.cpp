#include<iostream>
#include<string>
using namespace std;

int main()
{
    int num_tests; cin >> num_tests;
    for (int i=0; i < num_tests; i++) {
        int arr_len; cin >> arr_len;
        int previous=NULL;
        int current;
        int next;
        int flag = 0;
        int k_min;
        int k_max;
        string answer = "YES";
        for (int j=0; j < arr_len; j++) {
            cin >> current;
            if (previous==NULL) {}
            else if (previous > current) {
                if (flag) {
                    answer = "NO";
                    continue;
                }
                int k_min_proposal = previous - current; 
                if (k_min_proposal > k_min) {
                    k_min = k_min_proposal;
                }
            } else if (previous && previous)
            previous = current;
        }
        cout << answer << "\n";
    }
    return 0;
}