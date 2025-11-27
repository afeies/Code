package Java2.src;

public class Main {
    public static void main(String[] args){

        // Encapsulation = attributes of a class will be hidden or private,
        //                  Can be accessed only through methods (getters & setters)
        //                  You should make attributes provate if you don't have a reason to make them
        
        Car car = new Car("Chevrolet", "Camaro", 2021);
        
        // Error
        // System.out.println(car.make);
        System.out.println(car.getMake());

        // Error
        // car.year = 2022;
        car.setYear(2022);
        System.out.println(car.getYear());
    }
}
