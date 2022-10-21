using namespace std;
#include <iostream>
#include <vector>
class Solution {
public:
  vector<int> twoSum(const vector<int> &nums, int target) {
    for (int i = 0; i < nums.size() - 1; i++) {
      for (int j = i; j < nums.size(); j++) {
        int x = nums.at(i);
        int y = nums.at(j);
        if (j == i)
          continue;
        else if (x + y == target) {
          vector<int> res = {x, y};
          return res;
        }
      }
    }
    return {};
  }
};

int main() {
  Solution *x = new Solution();
  vector<int> vec = {1, 3, 5, 5, 5};
  vector<int> res = x->twoSum(vec, 10);
  for (auto &el : res) {
    cout << el << endl;
  }

  delete x;
}
