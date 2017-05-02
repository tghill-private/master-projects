#include <iostream>
using namespace std;

class animal {
    string name;
    int weight;
  public:
    animal (string, float);
    string colour;
    void set_weight( float new_weight );
    int get_weight () {return weight;}
    string get_name () {return name;}
};

animal::animal (string pet_name, float pet_weight):name(pet_name), weight(pet_weight) {};

void animal::set_weight( float new_weight ){
    weight = new_weight;
	}


int main(){
//    string lily="Lily";
//    string pet = "pet";
    animal animal1 ("lily", 20);
    animal animal2 ("pet", 12);

    string c1="Black";
    string c2 = "Brown";

    animal1.colour = c1;
    animal2.colour = c2;

    cout << "Animal 1 Name, weight, colour: " << animal1.get_name() << animal1.get_weight() << animal1.colour<<"\n";
    cout << "Animal 2 Name, weight colour:" << animal2.get_name() << animal2.get_weight() << animal2.colour <<"\n";

    animal1.set_weight(61);
    cout <<" Animal 1 Weight: " << animal1.get_weight() << "\n";

    return 0;
}
