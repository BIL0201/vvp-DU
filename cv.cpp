#include <string>
#include <iostream>

using namespace std;

class Person
{

    private:


    public:
        string name;
        int age;
        int birthnumber;
    Person(string name, int age, int birthnumber);
    
};

Person::Person (string n, int a, int b)
{
this->name = n;
this->age = a;
this->birthnumber = b;
}

int printname(Person person){

    cout << person.name << "\n";
return 0;

}

int number_control(Person person){

    if (person.birthnumber > 999999999)
    {
        if (person.birthnumber % 11 != 0)
        {
            cout << "wrong birthnumber" << "\n";

        }
    }
    return 0;
}


int main()
{
    Person p1("Martin", 27, 0205105142);
    printname(p1);
    number_control(p1);




}      