# include <iostream>
using namespace std;

class test {
 public:
  string name;
};

int void main() {
  test test_class;
  test_class.name = "First C++ Class";
  cout << "test.name = " << test_class.name <<"\n";

}
