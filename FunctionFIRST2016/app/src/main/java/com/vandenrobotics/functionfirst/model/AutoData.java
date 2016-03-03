package com.vandenrobotics.functionfirst.model;

import android.os.Parcel;
import android.os.Parcelable;

public class AutoData implements Parcelable {

    public boolean hadAuto;
    public boolean reachesDefences;
    public boolean crossesDefences;
    public boolean spybot;

    public int Defences1;

    public int bouldersInLowGoal;
    public int bouldersInHighGoal;

    public boolean hadOther;


    public AutoData(){
        hadAuto = false;
        reachesDefences = false;
        crossesDefences = false;
        spybot = false;

        bouldersInLowGoal = 0;
        bouldersInHighGoal = 0;

        hadOther = false;
    }

    public AutoData(String string){
        this();
        try{
            String[] dataString = string.split(",");


            int index = 0;

            hadAuto = Boolean.parseBoolean(dataString[index]);
            index += 1;
            reachesDefences = Boolean.parseBoolean(dataString[index]);
            index += 1;
            crossesDefences = Boolean.parseBoolean(dataString[index]);
            index += 1;
            spybot =Boolean.parseBoolean(dataString[index]);
            index += 1;
            Defences1 = Integer.parseInt(dataString[index]);
            index += 1;
            bouldersInLowGoal = Integer.parseInt(dataString[index]);
            index += 1;
            bouldersInHighGoal = Integer.parseInt(dataString[index]);
            index += 1;
            hadOther = Boolean.parseBoolean(dataString[index]);


        } catch (IndexOutOfBoundsException e){
            e.printStackTrace();
        }
    }

    public AutoData(AutoData autoData){
        this();
        hadAuto = autoData.hadAuto;
        reachesDefences = autoData.reachesDefences;
        crossesDefences = autoData.crossesDefences;
        spybot = autoData.spybot;
        Defences1 = autoData.Defences1;
        //Defences2 = autoData.Defences2;
        bouldersInLowGoal = autoData.bouldersInLowGoal;
        bouldersInHighGoal = autoData.bouldersInHighGoal;
        hadOther = autoData.hadOther;
    }

    @Override
    public String toString(){

        return hadAuto+","+reachesDefences+","+crossesDefences+","+spybot+","+Defences1+
                bouldersInLowGoal+","+bouldersInHighGoal+","+hadOther;
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
        public AutoData createFromParcel(Parcel in){
            return new AutoData(in.readString());
        }

        public AutoData[] newArray(int size){
            return new AutoData[size];
        }
    };
}
