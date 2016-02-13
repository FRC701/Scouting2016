package com.vandenrobotics.functionfirst.model;

import android.os.Parcel;
import android.os.Parcelable;


import com.vandenrobotics.functionfirst.R;

/**
 * Created by Programming701-A on 2/8/2016.
 */
public class PitData implements Parcelable {

    public int Team;

    public String Answer1;
    public String Answer2;
    public String Answer3;

    public PitData(){
        Team = 0;


    }

    public PitData(String string){
        this();
        try{
            String[] dataString = string.split("\\$");
            int index = 0;
            Team = Integer.parseInt(dataString[index]);
            index += 1;
            Answer1 = dataString[index];
            index += 1;
            Answer2 = dataString[index];
            index += 1;
            Answer3 = dataString[index];




        } catch (IndexOutOfBoundsException e){
            e.printStackTrace();
        }
    }

    public PitData(PitData pitData){
        this();
        Team = pitData.Team;
        Answer1 = pitData.Answer1;
        Answer2 = pitData.Answer2;
        Answer3 = pitData.Answer3;

    }

    @Override
    public String toString(){

        return Team+","+Answer1+","+Answer2+","+Answer3;
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
        public PitData createFromParcel(Parcel in){
            return new PitData(in.readString());
        }

        public  PitData[] newArray(int size){
            return new PitData[size];
        }
    };
}
