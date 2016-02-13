package com.vandenrobotics.functionfirst.activities;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;

import com.vandenrobotics.functionfirst.R;
import com.vandenrobotics.functionfirst.model.PitTeamData;
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
    private Spinner Team;

    private ArrayList<EditText> Answers;
    public EditText Answer1;
    public EditText Answer2;
    public EditText Answer3;
    public EditText Answer4;
    public EditText Answer5;
    public EditText Answer6;

    private ArrayList<PitTeamData> pitData;

    private int teamSelected;
    private int indexTeamSelected;


    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.pit_scouting);

        //Array of EditText, storing for easy calling of getText method
        Answers = new ArrayList<>(6);

        mEvent = getIntent().getStringExtra("event");

        Answer1 = (EditText) findViewById(R.id.answer_1);
        Answers.add(Answer1);

        Answer2 = (EditText) findViewById(R.id.answer_2);
        Answers.add(Answer2);

        Answer3 = (EditText) findViewById(R.id.answer_3);
        Answers.add(Answer3);

        Answer4 = (EditText) findViewById(R.id.answer_4);
        Answers.add(Answer4);

        Answer5 = (EditText) findViewById(R.id.answer_5);
        Answers.add(Answer5);

        Answer6 = (EditText) findViewById(R.id.answer_6);
        Answers.add(Answer6);

        //Event passed by Option Screen. Use for writing to file path
        mEvent = getIntent().getStringExtra("event");

        //Loads info for spinner
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

        //Sets array of items in spinner depending on number of teams
        teamAdapter = new ArrayAdapter<>(this, R.layout.spinner_base, team_numbers);
        teamAdapter.setDropDownViewResource(R.layout.spinner_dropdown);

        //Links spinner all together
        Team = (Spinner)findViewById(R.id.spinnerTeamNumberP);
        Team.setAdapter(teamAdapter);
        Team.setSelection(teamAdapter.getPosition(team_numbers.get(0)));
        Team.setOnItemSelectedListener(this);

    }

    //Runs when button is clicked
    public void Submit(View view){

        saveData();

        //Don't see necessity to destroy activity. Unlikely we will leave while pit scouting
        /*
        Intent intent = new Intent(this, PitScoutActivity.class);
        intent.putExtra("event", mEvent);

        startActivity(intent);
        this.finish();
        */
    }

    //Load data depending on what team is selected
    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        //Get the team selected
        teamSelected = team_numbers.get(position);
        //Get index of the team selected
        indexTeamSelected = position;
        //If read data save about that team, will return " " in none found, can be change in TeamPitData
        readData();

    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }

    private void saveData(){
        updateData();
        ExternalStorageTools.writePitData(pitData,mEvent);

    }

    //read data from file at /ScoutData/mEvent/pitdata.txt
    private void readData() {
        //call readData function from ExternalStorageTools, giving even and number of teams,
        // for creating numberOfTeams TeamPitData objects
        pitData = ExternalStorageTools.readPitData(team_numbers.size(), mEvent);

        Answer1.setText(pitData.get(indexTeamSelected).answer1);
        Answer2.setText(pitData.get(indexTeamSelected).answer2);
        Answer3.setText(pitData.get(indexTeamSelected).answer3);
        Answer4.setText(pitData.get(indexTeamSelected).answer4);
        Answer5.setText(pitData.get(indexTeamSelected).answer5);
        Answer6.setText(pitData.get(indexTeamSelected).answer6);

    }

    public void updateData(){

        pitData.get(indexTeamSelected).team = "" + teamSelected;
        pitData.get(indexTeamSelected).answer1 = "" + Answer1.getText();
        pitData.get(indexTeamSelected).answer2 = "" + Answer2.getText();
        pitData.get(indexTeamSelected).answer3 = "" + Answer3.getText();
        pitData.get(indexTeamSelected).answer4 = "" + Answer4.getText();
        pitData.get(indexTeamSelected).answer5 = "" + Answer5.getText();
        pitData.get(indexTeamSelected).answer6 = "" + Answer6.getText();

    }

}

