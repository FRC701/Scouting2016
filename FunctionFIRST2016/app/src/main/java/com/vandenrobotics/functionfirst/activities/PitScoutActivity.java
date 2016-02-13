package com.vandenrobotics.functionfirst.activities;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;

import com.vandenrobotics.functionfirst.R;
import com.vandenrobotics.functionfirst.tools.ExternalStorageTools;
import com.vandenrobotics.functionfirst.tools.JSONTools;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.Collections;

/**
 * Created by Programming701-A on 1/13/2016.
 */
public class PitScoutActivity extends Activity implements Spinner.OnItemSelectedListener{

    public String mEvent;

    private ArrayList<Integer> team_numbers;

    private ArrayAdapter<Integer> teamAdapter;
    private Spinner spinnerTeams;

    public EditText Answer1;
    public EditText Answer2;
    public EditText Answer3;
    public EditText Answer4;
    public EditText Answer5;
    public EditText Answer6;

    private int teamSelected;

    private String[] pitData;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.pit_scouting);

        pitData = new String[7];

        Answer1 = (EditText) findViewById(R.id.answer_1);
        Answer2 = (EditText) findViewById(R.id.answer_2);
        Answer3 = (EditText) findViewById(R.id.answer_3);
        Answer4 = (EditText) findViewById(R.id.answer_4);
        Answer5 = (EditText) findViewById(R.id.answer_5);
        Answer6 = (EditText) findViewById(R.id.answer_6);


        mEvent = getIntent().getStringExtra("event");

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

        teamAdapter = new ArrayAdapter<>(this, R.layout.spinner_base, team_numbers);
        teamAdapter.setDropDownViewResource(R.layout.spinner_dropdown);

        spinnerTeams = (Spinner)findViewById(R.id.spinnerTeamNumberP);
        spinnerTeams.setAdapter(teamAdapter);
        spinnerTeams.setSelection(teamAdapter.getPosition(team_numbers.get(0)));
        spinnerTeams.setOnItemSelectedListener(this);

        readData(teamSelected);

    }

    public void submit(View view){

        saveData();
        ExternalStorageTools.writePitData(pitData, mEvent);

        /*
        Intent intent = new Intent(this, PitScoutActivity.class);
        intent.putExtra("event", mEvent);

        startActivity(intent);
        this.finish();
        */
    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        teamSelected = team_numbers.get(position);
        readData(teamSelected);
    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }

    private void saveData(){

        int index = 0;
        pitData[index] = "" + teamSelected;
        index++;
        pitData[index] = "" + Answer1.getText();
        index++;
        pitData[index] = "" + Answer2.getText();
        index++;
        pitData[index] = "" + Answer3.getText();
        index++;
        pitData[index] = "" + Answer4.getText();
        index++;
        pitData[index] = "" + Answer5.getText();
        index++;
        pitData[index] = "" + Answer6.getText();

    }

    private void readData(int teamSelected){
        pitData = ExternalStorageTools.readPitData(teamSelected, mEvent); //Return an array and stores in our pitData
    }

}

