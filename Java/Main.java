package Java;

interface Animal{
    void makeSound();
}

class Dog implements Animal {
    public void makeSound() {System.out.println("bark");}
}

class Cow implements Animal {
    public void makeSound() {moo();}
    public void moo() {System.out.println("moo!");}
}

public final class Main {
    public static void main(String[] args) {
        Animal x = new Animal() {
            public void makeSound() {
                System.out.println("chirp!");
            }
        };

        x.makeSound();
        Animal d = new Dog();
        d.makeSound();

        Cow c = new Cow();
        c.makeSound();
        c.moo();

        // Animal a = new Animal();
    }
}