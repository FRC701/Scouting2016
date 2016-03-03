package com.vandenrobotics.functionfirst.model;

import android.os.Parcel;
import android.os.Parcelable;

import java.util.ArrayList;

/**
 * Created by Programming701-A on 1/31/2015.
 */
public class TeleData implements Parcelable {

    public String LowBar;
    public String TeleDefence1;
    public String TeleDefence2;
    public String TeleDefence3;
    public String TeleDefence4;

    public int P_DamageCounterTele1;
    public int P_DamageCounterTele2;
    public int P_DamageCounterTele3;
    public int P_DamageCounterTele4;
    public int P_DamageCounterTele5;

    public int BouldersInLowGoal;
    public int BouldersLowGoalMissed;
    public int BouldersInHighGoal;
    public int BouldersHighGoalMissed;



    public TeleData(){

        TeleDefence1 = "Category 1";
        TeleDefence2 = "Category 2";
        TeleDefence3 = "Category 3";
        TeleDefence4 = "Category 4";

        P_DamageCounterTele1 = 0;
        P_DamageCounterTele2 = 0;
        P_DamageCounterTele3 = 0;
        P_DamageCounterTele4 = 0;
        P_DamageCounterTele5 = 0;

        BouldersInLowGoal = 0;
        BouldersLowGoalMissed = 0;
        BouldersInHighGoal = 0;
        BouldersHighGoalMissed = 0;


    }

    public TeleData(String string){
        this();
        try{
            String[] dataString = string.split(",");

            int index = 0;

            LowBar = dataString[index];
            index += 1;
            P_DamageCounterTele1 = Integer.parseInt(dataString[index]);
            index += 1;
            TeleDefence1 = dataString[index];
            index += 1;
            P_DamageCounterTele2 =   Integer.parseInt(dataString[index]);
            index += 1;
            TeleDefence2 = dataString[index];
            index += 1;
            P_DamageCounterTele3 =  Integer.parseInt(dataString[index]);
            index += 1;
            TeleDefence3 = dataString[index];
            index += 1;
            P_DamageCounterTele4 =  Integer.parseInt(dataString[index]);
            index += 1;
            TeleDefence4 = dataString[index];
            index += 1;
            P_DamageCounterTele5 =  Integer.parseInt(dataString[index]);
            index += 1;
            BouldersInLowGoal =  Integer.parseInt(dataString[index]);
            index += 1;
            BouldersLowGoalMissed = Integer.parseInt(dataString[index]);
            index += 1;
            BouldersInHighGoal =  Integer.parseInt(dataString[index]);
            index += 1;
            BouldersHighGoalMissed = Integer.parseInt(dataString[index]);




        } catch (IndexOutOfBoundsException e){
            e.printStackTrace();
        }
    }

    public TeleData(TeleData teleData) {
        this();

        LowBar = teleData.LowBar;
        TeleDefence1 = teleData.TeleDefence1;
        TeleDefence2 = teleData.TeleDefence2;
        TeleDefence3 = teleData.TeleDefence3;
        TeleDefence4 = teleData.TeleDefence4;

        P_DamageCounterTele1 = teleData.P_DamageCounterTele1;
        P_DamageCounterTele2 = teleData.P_DamageCounterTele2;
        P_DamageCounterTele3 = teleData.P_DamageCounterTele3;
        P_DamageCounterTele4 = teleData.P_DamageCounterTele4;
        P_DamageCounterTele5 = teleData.P_DamageCounterTele5;

        BouldersInLowGoal = teleData.BouldersInLowGoal;
        BouldersLowGoalMissed = teleData.BouldersLowGoalMissed;
        BouldersInHighGoal = teleData.BouldersInHighGoal;
        BouldersHighGoalMissed = teleData.BouldersHighGoalMissed;


    }

    @Override
    public String toString(){



         return  LowBar+","+P_DamageCounterTele1+","+TeleDefence1+","+P_DamageCounterTele2+","+
                 TeleDefence2+","+P_DamageCounterTele3+","+TeleDefence3+","+P_DamageCounterTele4+"," +TeleDefence4
                 +","+P_DamageCounterTele5+","+BouldersInLowGoal+","+BouldersLowGoalMissed+","+BouldersInHighGoal+","+BouldersHighGoalMissed;

    }

    @Override
    public int describeContents() {
        // TODO Auto-generated method stub
        return 0;
    }

    @Override
    public void writeToParcel(Parcel arg0, int arg1) {
        // TODO Auto-generated method stub
        arg0.writeString(this.toString());
    }

    public static final Parcelable.Creator CREATOR = new Parcelable.Creator() {
        public TeleData createFromParcel(Parcel in){
            return new TeleData(in.readString());
        }

        public TeleData[] newArray(int size){
            return new TeleData[size];
        }
    };
}
