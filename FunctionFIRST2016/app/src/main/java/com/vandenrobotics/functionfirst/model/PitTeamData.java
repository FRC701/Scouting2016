package com.vandenrobotics.functionfirst.model;

import java.util.ArrayList;


public class PitTeamData {

    //Creating variable to hold each teams pitData
    public String team;

    public String answer1;
    public String answer2;
    public String answer3;
    public String answer4;
    public String answer5;
    public String answer6;

    public PitTeamData(){
        //If will display text " " by default, can be changed to have hit
        team = "0";
        answer1 = " ";
        answer2 = " ";
        answer3 = " ";
        answer4 = " ";
        answer5 = " ";
        answer6 = " ";
    }

    public PitTeamData(String string){

        String[] dataString = string.split("\\$");

        team = dataString[0];

        answer1 = dataString[1];
        answer2 = dataString[2];
        answer3 = dataString[3];
        answer4 = dataString[4];
        answer5 = dataString[5];
        answer6 = dataString[6];

    }

    public String toString(){
        return team + "$" + answer1 + "$" + answer2 + "$" +  answer3 + "$" + answer4 + "$"
                + answer5 + "$" + answer6 + "\n";
    }

}

