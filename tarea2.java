package tarea2_121;

import java.awt.*;
import javax.swing.*;

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
        double angulo = Math.atan2(y, x);
        return new double[]{radio, angulo};
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}

class Linea {
    Punto p1, p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public void dibujarLinea(Graphics g) {
        g.drawLine(p1.x * 20, p1.y * 20, p2.x * 20, p2.y * 20);
    }

    @Override
    public String toString() {
        return "Punto 1: " + p1 + ", Punto 2: " + p2;
    }
}

class Circulo {
    Punto centro;
    int radio;

    public Circulo(Punto centro, int radio) {
        this.centro = centro;
        this.radio = radio;
    }

    public void dibujarCirculo(Graphics g) {
        g.drawOval(centro.x * 20 - radio * 20, centro.y * 20 - radio * 20, radio * 40, radio * 40);
    }

    @Override
    public String toString() {
        return "Centro: " + centro + ", Radio: " + radio;
    }
}

public class tarea2 extends JPanel {
    Punto punto1 = new Punto(2, 3);
    Punto punto2 = new Punto(4, 5);
    Linea linea = new Linea(punto1, punto2);
    Circulo circulo = new Circulo(punto1, 2);

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        circulo.dibujarCirculo(g);
        linea.dibujarLinea(g);
    }

    public static void main(String[] args) {
        Punto punto1 = new Punto(2, 3);
        Punto punto2 = new Punto(4, 5);
        Linea linea = new Linea(punto1, punto2);
        Circulo circulo = new Circulo(punto1, 2);

        int[] cartesianas = punto1.coordCartesianas();
        double[] polares = punto1.coordPolares();

        System.out.println("Coordenadas cartesianas:");
        System.out.println(cartesianas[0] + " " + cartesianas[1]);

        System.out.println("Coordenadas polares:");
        System.out.println(polares[0] + " " + polares[1]);

        System.out.println(punto1 + "  Punto 1");
        System.out.println(punto2 + "  Punto 2");
        System.out.println(linea + "  Línea");

        JFrame frame = new JFrame();
        tarea2 dibujo = new tarea2();
        frame.add(dibujo);
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
