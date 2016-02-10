package com.vandenrobotics.functionfirst.activities;

import android.app.Activity;
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

import java.util.ArrayList;
import java.util.Collections;

/**
 * Created by Programming701-A on 1/13/2016.
 */
public class PitScoutActivity extends Activity {

    public String mEvent;
    public int mTeamNumber;
    private ArrayList<Integer> team_numbers;
    private ArrayAdapter<Integer> teamAdapter;
    private Spinner Team;

    private boolean viewsAssigned = false;

    public PitData mPitData;
    public EditText Answer1;
    public EditText Answer2;
    public EditText Answer3;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.pit_scouting);
        mEvent = getIntent().getStringExtra("event");
        mTeamNumber = getIntent().getIntExtra("teamNumber", 0);

        ArrayList<JSONObject> teamInfo = ExternalStorageTools.readTeams(mEvent);

        teamInfo = JSONTools.sortJSONArray(teamInfo, "team_number");
        team_numbers = new ArrayList<>(teamInfo.size());
        try {
            for (int i = 0; i < teamInfo.size(); i++) {
                team_numbers.add(i, teamInfo.get(i).getInt("team_number"));
            }
        } catch (JSONException e){
            e.printStackTrace();
        }

        Collections.sort(team_numbers);
        assignViews(view);

        if (viewsAssigned) loadData(mPitData);
    }

    @Override
    public void onPause(){
        super.onPause();
        mPitData = new PitData(saveData());
        viewsAssigned=false;
    }

    @Override
    public void onResume(){
        super.onResume();
        assignViews(getView);
        if(viewsAssigned) loadData(mPitData);
    }

    public void Submit(View view){
        mPitData = new PitData(saveData());
    }

    public void loadData(final PitData pitData){
        // take the autoData and assign it to each view
        Team.setSelection(pitData.Team);
        Answer1.setText(pitData.Answer1);
        Answer2.setText(pitData.Answer2);
        Answer3.setText(pitData.Answer3);
    }

    public PitData saveData(){
        PitData pitData = new PitData();
        if(viewsAssigned){
            pitData.Team = Team.getSelectedItemPosition();
            pitData.Answer1 = Answer1.getText().toString();
            pitData.Answer2 = Answer2.getText().toString();
            pitData.Answer3 = Answer3.getText().toString();
        }

        return pitData;
    }

    private void assignViews(View view){
        try {
            Team = (Spinner)findViewById(R.id.spinnerTeamNumberP);
            teamAdapter = new ArrayAdapter<>(this, R.layout.spinner_base, team_numbers);
            teamAdapter.setDropDownViewResource(R.layout.spinner_dropdown);
            Team.setAdapter(teamAdapter);
            Team.setSelection(teamAdapter.getPosition(mTeamNumber));

            Answer1 = (EditText)view.findViewById(R.id.answer_1);
            Answer2 = (EditText)view.findViewById(R.id.answer_2);
            Answer3 = (EditText)view.findViewById(R.id.answer_3);


            viewsAssigned = true;
        } catch (Exception e){
            e.printStackTrace();
            viewsAssigned = false;
    }
}
}
