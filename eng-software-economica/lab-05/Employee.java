import java.util.ArrayList;

public class Employee extends TemplateMethod {
    private ArrayList<String> routines;

    public Employee() {
        this.routines = new ArrayList<>();
    }

    protected void addRoutine(String routine) {
        routines.add(routine);
    }

    @Override
    protected void printRoutine() {
        for (String routine : this.routines) {
            System.out.println(routine);
        }
    }

}
