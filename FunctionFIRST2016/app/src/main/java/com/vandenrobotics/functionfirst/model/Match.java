package com.vandenrobotics.functionfirst.model;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by Joey on 2/8/2015.
 */
public class Match {
    public int number;
    public int[] teams;

    public Match(){
        number = 0;
        teams = new int[6];
    }

    public Match(JSONObject singlematch){
        try {
            int matchnumber = singlematch.getInt("match_number");
            JSONObject alliances = singlematch.getJSONObject("alliances");
            JSONObject red = alliances.getJSONObject("red");
            JSONObject blue = alliances.getJSONObject("blue");
            number = matchnumber;
            teams[0] = red.get(0).toString();

            /*
            JSONArray teamR = red.getJSONArray("teams");
            teams[0] = teamR.getInt(0);
            teams[1] = teamR.getInt(1);
            teams[2] = teamR.getInt(2);
            JSONArray teamB = blue.getJSONArray("teams");
            teams[3] = teamB.getInt(0);
            teams[4] = teamB.getInt(1);
            teams[5] = teamB.getInt(2);*/

            

        } catch (JSONException e) {
            e.printStackTrace();
        }catch (NullPointerException e){
            e.printStackTrace();
        }
    }

    public Match(String s) {
        try {
            String[] info = s.split(",");
            number = Integer.parseInt(info[0]);
            teams[0] = Integer.parseInt(info[1]);
            teams[1] = Integer.parseInt(info[2]);
            teams[2] = Integer.parseInt(info[3]);
            teams[3] = Integer.parseInt(info[4]);
            teams[4] = Integer.parseInt(info[5]);
            teams[5] = Integer.parseInt(info[6]);
        } catch (IndexOutOfBoundsException e){
            e.printStackTrace();
            number = 0;
            teams = new int[6];
        } catch (NumberFormatException e){
            e.printStackTrace();
            number = 0;
            teams = new int[6];
        }
    }

    public String toString(){
        return number + ","
                + teams[0] + ","
                + teams[1] + ","
                + teams[2] + ","
                + teams[3] + ","
                + teams[4] + ","
                + teams[5] + "\n";
    }
}
