/**
file class.cpp

This file is for playing around with classes in C++
**/
#include <iostream>
using namespace std;

class animal {
  public:
    // animal (string pet_name, float pet_weight, string pet_colour): name(pet_name), weight(pet_weight), colour(colour) {};
    animal(string pet_name, float pet_weight, string pet_colour) {
      name = pet_name;
      weight = pet_weight;
      colour = pet_colour;
    };

    int get_weight () {return weight;
    };
    void set_weight( float new_weight ) {
      weight = new_weight;
    };

    string get_name () {return name;
    };
    void set_name(string new_name) {
      name = new_name;
    };

    string get_colour () {return colour;
    };
    void set_colour(string new_colour) {
      colour = new_colour;
    };

  private:
    string name;
    int weight;
    string colour;
};


int main(){
//    string lily="Lily";
//    string pet = "pet";
    animal animal1 ("lily", 20, "Black");
    animal animal2 ("pet", 12, "Brown");

    cout << "Animal 1 Name, weight, colour: " << animal1.get_name() << animal1.get_weight() << animal1.get_colour()<<"\n";
    cout << "Animal 2 Name, weight colour:" << animal2.get_name() << animal2.get_weight() << animal2.get_colour() <<"\n";

    animal1.set_weight(61);
    cout <<" Animal 1 Weight: " << animal1.get_weight() << "\n";

    // cout <<"Animal 2 Colour: " << animal2.colour

    return 0;
}
