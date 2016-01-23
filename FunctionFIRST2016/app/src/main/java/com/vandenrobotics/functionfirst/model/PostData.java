package com.vandenrobotics.functionfirst.model;

import android.os.Parcel;
import android.os.Parcelable;

/**
 * Created by Programming701-A on 1/31/2015.
 */
public class PostData implements Parcelable {

    public int numFouls;
    public int numTechFouls;
    public boolean gotRedCard;
    public boolean gotYellowCard;
    public boolean wasDisabled;
    public boolean playedDefensively;
    public boolean capture;
    public boolean breached;
    public int challengeState;
    public int scaleState;


    public PostData(){
        numFouls = 0;
        numTechFouls = 0;
        gotRedCard = false;
        gotYellowCard = false;
        wasDisabled = false;
        playedDefensively = false;
        capture = false;
        breached = false;
        challengeState = 0;
        scaleState = 0;
    }

    public PostData(String string){
        this();
        try{
            String[] dataString = string.split(",");
            int[] data = new int[dataString.length];

            try{
                for(int i = 0; i < data.length; i++)
                    data[i] = Integer.parseInt(dataString[i]);
            } catch (NumberFormatException e){
                e.printStackTrace();
            } catch (IndexOutOfBoundsException e){
                e.printStackTrace();
            }

            numFouls = data[0];
            numTechFouls = data[1];
            gotRedCard = (data[2]==1);
            gotYellowCard = (data[3]==1);
            wasDisabled = (data[4]==1);
            playedDefensively = (data[5]==1);
            capture = (data[6]==1);
            breached = (data[7]==1);
            challengeState = data[8];
            scaleState= data[9];

        } catch (IndexOutOfBoundsException e){
            e.printStackTrace();
        }
    }

    public PostData(PostData postData) {
        this();
        numFouls = postData.numFouls;
        numTechFouls = postData.numTechFouls;
        gotRedCard = postData.gotRedCard;
        gotYellowCard = postData.gotYellowCard;
        wasDisabled = postData.wasDisabled;
        playedDefensively = postData.playedDefensively;
        capture = postData.capture;
        breached = postData.breached;
        challengeState = postData.challengeState;
        scaleState = postData.scaleState;
    }

    @Override
    public String toString(){
        int tempRedCard = gotRedCard? 1 : 0;
        int tempYellowCard = gotYellowCard? 1 : 0;
        int tempDisabled = wasDisabled? 1 : 0;
        int tempPlayedDefensively = playedDefensively? 1 : 0;
        int tempCapture = capture? 1 : 0;
        int tempBreached = breached? 1 : 0;

        return numFouls+","+numTechFouls+","+tempRedCard+","+tempYellowCard+","+tempDisabled+","+tempPlayedDefensively+","+tempCapture+","+tempBreached+","+challengeState+","+scaleState;
    }

    @Override
    public int describeContents() {
        // TODO auto-generated method stub
        return 0;
    }

    @Override
    public void writeToParcel(Parcel arg0, int arg1) {
        // TODO auto-generated method stub
        arg0.writeString(this.toString());
    }

    public static final Parcelable.Creator CREATOR = new Parcelable.Creator() {
        public PostData createFromParcel(Parcel in){
            return new PostData(in.readString());
        }

        public PostData[] newArray(int size){
            return new PostData[size];
        }
    };
}
