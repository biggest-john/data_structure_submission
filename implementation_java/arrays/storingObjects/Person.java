package arrays.storingObjects;

public class Person {
    private String lastName;
    private String firstName;
    private int age;

    Person(String last, String first, int a){
        lastName = last;
        firstName = first;
        age = a;
    }

    public void displayPerson(){
        System.out.print("   Last name: " + lastName);
        System.out.print(", First name: " + firstName);
        System.out.println(", Age: " + age);
    }

    public String getLast(){
        return lastName;
    }
}
