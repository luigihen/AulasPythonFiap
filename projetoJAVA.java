package com.java;

import java.util.Scanner;



public class prova {
	public static void main(String[] args) {
		
		float checkpoint = 0;
		float checkpoint1 = 0;
		float checkpoint2 = 0;
		
		float sprint = 0;
		float sprint1 = 0;
		
		
		float globalsolution = 0;
		
		Scanner sc = new Scanner(System.in);
		System.out.println("digite a nota(até uma casa decimal) do primeiro checkpoint");
		checkpoint = sc.nextFloat();
		
		Scanner sc1 = new Scanner(System.in);
		System.out.println("digite a nota(até uma casa decimal) do segundo checkpoint");
		checkpoint1 = sc1.nextFloat();
		
		Scanner sc2 = new Scanner(System.in);
		System.out.println("digite a nota(até uma casa decimal) do terceiro checkpoint");
		checkpoint2 = sc2.nextFloat();
		
		Scanner sc3 = new Scanner(System.in);
		System.out.println("digite a nota(até uma casa decimal) da primeira sprint");
		sprint = sc3.nextFloat();
		
		Scanner sc4 = new Scanner(System.in);
		System.out.println("digite a nota(até uma casa decimal) da segunda sprint");
		sprint = sc4.nextFloat();
		
		Scanner sc5 = new Scanner(System.in);
		System.out.println("digite a nota(até uma casa decimal) da global solution");
		sprint = sc5.nextFloat();
		
		float menor = checkpoint;
		if(checkpoint1 <= checkpoint) {
			menor = checkpoint1;
		}
		if(checkpoint2 <= checkpoint) {
			menor = checkpoint2;
		}
		
		double media = ([checkpoint + checkpoint1 + checkpoint2 - menor + sprint + sprint1 ]/4) * 0.4 + globalsolution * 0.6;
		double mediapeso = media * 0.4;
		
		System.out.println(media);
		System.out.println(mediapeso);
		
		
		

		
		
		
	}
}