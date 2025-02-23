package tarea2_121;

import java.lang.Math;

class Punto {
    int x, y;

    public Punto(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int[] coordCartesianas() {
        return new int[]{x, y};
    }

    public double[] coordPolares() {
        double radio = Math.sqrt(x * x + y * y);
        double angulo = Math.atan(x / (double) y);
        return new double[]{radio, angulo};
    }

    @Override
    public String toString() {
        return x + " " + y;
    }
}

public class tarea1 {
    public static void main(String[] args) {
        Punto punto1 = new Punto(2, 3);
        int[] cartesianas = punto1.coordCartesianas();
        System.out.println(cartesianas[0] + " " + cartesianas[1]);

        double[] polares = punto1.coordPolares();
        System.out.println(polares[0] + " " + polares[1]);

        System.out.println(punto1);
    }
}
