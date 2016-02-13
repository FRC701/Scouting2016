package com.vandenrobotics.functionfirst.activities;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;

import com.vandenrobotics.functionfirst.R;
import com.vandenrobotics.functionfirst.model.PitData;
import com.vandenrobotics.functionfirst.tools.ExternalStorageTools;
import com.vandenrobotics.functionfirst.tools.JSONTools;

import org.json.JSONException;
import org.json.JSONObject;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Collections;

/**
 * Created by Programming701-A on 1/13/2016.
 */
public class PitScoutActivity extends Activity implements Spinner.OnItemSelectedListener{

    public String mEvent;
    private ArrayList<Integer> team_numbers;
    private ArrayAdapter<Integer> teamAdapter;
    private Spinner Team;

    private String[] PitData;

    private int teamSelected;

    public EditText Answer1;
    public EditText Answer2;
    public EditText Answer3;
    public EditText Answer4;
    public EditText Answer5;
    public EditText Answer6;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.pit_scouting);
        mEvent = getIntent().getStringExtra("event");
        //mPitDataList = getIntent().getParcelableArrayListExtra("pitData");


        PitData = new String[7];

        ArrayList<JSONObject> teamInfo = ExternalStorageTools.readTeams(mEvent);

        teamInfo = JSONTools.sortJSONArray(teamInfo, "team_number");
        team_numbers = new ArrayList<>(teamInfo.size());
        try {
            for (int i = 0; i < teamInfo.size(); i++) {
                team_numbers.add(i, teamInfo.get(i).getInt("team_number"));
            }
        } catch (JSONException e) {
            e.printStackTrace();
        }

        Collections.sort(team_numbers);

        Team = (Spinner) findViewById(R.id.spinnerTeamNumberP);
        teamAdapter = new ArrayAdapter<>(this, R.layout.spinner_base, team_numbers);
        teamAdapter.setDropDownViewResource(R.layout.spinner_dropdown);
        Team.setAdapter(teamAdapter);
        Team.setSelection(teamAdapter.getPosition(team_numbers.get(0)));
        Team.setOnItemSelectedListener(this);

        Answer1 = (EditText) findViewById(R.id.answer_1);
        Answer2 = (EditText) findViewById(R.id.answer_2);
        Answer3 = (EditText) findViewById(R.id.answer_3);
        Answer4 = (EditText) findViewById(R.id.answer_4);
        Answer5 = (EditText) findViewById(R.id.answer_5);
        Answer6 = (EditText) findViewById(R.id.answer_6);

        readData(teamSelected);
    }

    public void Submit(View view) {

        saveData();

        ExternalStorageTools.writePitData(PitData, mEvent);

       /** Intent intent = new Intent(this, PitScoutActivity.class);
        intent.putExtra("event", mEvent);

        startActivity(intent);
        this.finish(); */
    }


    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        teamSelected = team_numbers.get(position);
        readData(teamSelected);
    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }

    private void readData(int teamSelected){
      PitData = ExternalStorageTools.readPitData(teamSelected, mEvent); //return an array and stores in our pitData
    }
    private void saveData(){

        int index = 0;
        PitData[index] = "" + teamSelected;
        index +=1;
        PitData[index] =  Answer1.getText().toString();
        index +=1;
        PitData[index] =  Answer2.getText().toString();
        index +=1;
        PitData[index] =  Answer3.getText().toString();
        index +=1;
        PitData[index] =  Answer4.getText().toString();
        index +=1;
        PitData[index] =  Answer5.getText().toString();
        index +=1;
        PitData[index] =  Answer6.getText().toString();

    }
}