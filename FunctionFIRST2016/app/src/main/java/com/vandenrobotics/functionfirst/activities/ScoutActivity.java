package com.vandenrobotics.functionfirst.activities;

import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.pm.ResolveInfo;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.Spinner;
import android.widget.Toast;

import com.vandenrobotics.functionfirst.R;
import com.vandenrobotics.functionfirst.model.Match;
import com.vandenrobotics.functionfirst.model.MatchData;
import com.vandenrobotics.functionfirst.tools.ExternalStorageTools;
import com.vandenrobotics.functionfirst.tools.JSONTools;
import com.vandenrobotics.functionfirst.views.NumberPicker;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ScoutActivity extends Activity {

    private String mEvent;
    private String mMatches;
    private int mDeviceNumber;
    private int mCurMatch;
    private int mTeamNumber;
    private ArrayList<Integer> team_numbers;

    private ArrayList<Match> mMatchList;
    private ArrayList<MatchData> mMatchData;

    private Spinner spinnerDevices;
    private ArrayAdapter<CharSequence> deviceAdapter;
    private NumberPicker pickerMatches;
    private static Spinner spinnerTeams;
    private ArrayAdapter<Integer> teamAdapter;
    private CheckBox DataTransfer;
    private Button SendViaBluetooth;

    private final int MAX_MATCHES = 200; // a reasonable amount of matches to expect any event to have less than
    private static final int DISCOVER_DURATION = 300;
    private static final int REQUEST_BLU = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_scout);
        mEvent = getIntent().getStringExtra("event");
        mMatchList = ExternalStorageTools.readMatches(mEvent);
        mDeviceNumber = ExternalStorageTools.readDevice(mEvent);
        mCurMatch = ExternalStorageTools.readCurrentMatch(mEvent, mDeviceNumber);
        mMatchData = ExternalStorageTools.readData(mEvent, mDeviceNumber);

        SendViaBluetooth = (Button)findViewById(R.id.button_sendData);
        SendViaBluetooth.setEnabled(false);
        DataTransfer = (CheckBox)findViewById(R.id.checkBox_enableDataTransfer);
        DataTransfer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (DataTransfer.isChecked())
                    enableDataTransfer();
                else
                    diableDataTransfer();
            }
        });

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

        spinnerDevices = (Spinner)findViewById(R.id.spinnerDeviceNumber);
        deviceAdapter = ArrayAdapter.createFromResource(this, R.array.deviceOptions, R.layout.spinner_base);
        deviceAdapter.setDropDownViewResource(R.layout.spinner_dropdown);
        spinnerDevices.setAdapter(deviceAdapter);
        spinnerDevices.setSelection(mDeviceNumber - 1);

        pickerMatches = (NumberPicker)findViewById(R.id.pickerMatch);
        pickerMatches.something(true);
        pickerMatches.setMinValue(1);
        pickerMatches.setMaxValue(MAX_MATCHES);
        pickerMatches.setValue(mCurMatch);

        spinnerTeams = (Spinner)findViewById(R.id.spinnerTeamNumber);
        teamAdapter = new ArrayAdapter<>(this, R.layout.spinner_base, team_numbers);
        teamAdapter.setDropDownViewResource(R.layout.spinner_dropdown);
        spinnerTeams.setAdapter(teamAdapter);
        spinnerTeams.setSelection(teamAdapter.getPosition(mTeamNumber));

        spinnerDevices.setOnItemSelectedListener(new Spinner.OnItemSelectedListener(){
            @Override
            public void onItemSelected(AdapterView<?> adapter, View v, int position, long arg3) {
                mDeviceNumber=spinnerDevices.getSelectedItemPosition()+1;
                mCurMatch = ExternalStorageTools.readCurrentMatch(mEvent, mDeviceNumber);
                mTeamNumber = (mMatchList.size()>0)? mMatchList.get(mCurMatch-1).teams[mDeviceNumber - 1] : 0;

                pickerMatches.setValue(mCurMatch);
                spinnerTeams.setSelection(teamAdapter.getPosition(mTeamNumber));
            }

            @Override
            public void onNothingSelected(AdapterView<?> adapter){

            }
        });

        spinnerTeams.setOnItemSelectedListener(new Spinner.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapter, View v, int position, long arg3) {
                mTeamNumber = Integer.parseInt(spinnerTeams.getItemAtPosition(position).toString());
            }

            @Override
            public void onNothingSelected(AdapterView<?> adapter) {

            }
        });
    }

    public void activityMatch(View view) {
        // load the new match, passing all the info to it
        mDeviceNumber = spinnerDevices.getSelectedItemPosition() + 1;
        ExternalStorageTools.writeDevice(mDeviceNumber, mEvent);
        mCurMatch = pickerMatches.getValue();

           // if (ExternalStorageTools.readCurrentMatch(mEvent, mDeviceNumber) == mCurMatch - 1) {
                ExternalStorageTools.writeCurrentMatch(mCurMatch, mEvent, mDeviceNumber);
                mTeamNumber = (int) spinnerTeams.getSelectedItem();
                Intent intent = new Intent(this, MatchActivity.class);
                try {
                    intent.putExtra("event", mEvent);
                    intent.putExtra("matchNumber", mCurMatch);
                    intent.putExtra("teamNumber", mTeamNumber);
                    intent.putExtra("deviceNumber", mDeviceNumber);
                    intent.putExtra("matchData", mMatchData);
                } catch (IndexOutOfBoundsException e) {
                    e.printStackTrace();
                }
                startActivity(intent);
                this.finish();
           // }
        /*
            else if (ExternalStorageTools.readCurrentMatch(mEvent, mDeviceNumber) != mCurMatch - 1){
                if (ExternalStorageTools.readCurrentMatch(mEvent, mDeviceNumber) < mCurMatch){
                    int savedmatch = ExternalStorageTools.readCurrentMatch(mEvent,mDeviceNumber);
                    int differenceofmatches = mCurMatch - savedmatch;
                    for (int i = 0; i < differenceofmatches; i++){
                        ArrayList<Match> nullmatches = new ArrayList<Match>();
                        nullmatches.set(0, Match.nullMatch);

                    }
                }
        }*/

    }
    public static void upDateTeam(int currentMatch){

        spinnerTeams.setSelection(currentMatch);

    }

    public void sendDataViaBluetooth(View v) {
        BluetoothAdapter btAdapter = BluetoothAdapter.getDefaultAdapter();

        if (btAdapter == null) {
            Toast.makeText(this, "Bluetooth is not supported on this device", Toast.LENGTH_LONG).show();
        } else {
            enableBluetooth();
        }

    }
    public void enableBluetooth(){
        Intent discoveryIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_DISCOVERABLE);

        discoveryIntent.putExtra(BluetoothAdapter.EXTRA_DISCOVERABLE_DURATION, DISCOVER_DURATION);

        startActivityForResult(discoveryIntent, REQUEST_BLU);
    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data){

        if(resultCode == DISCOVER_DURATION && requestCode == REQUEST_BLU){

            Intent intent = new Intent();
            intent.setAction(Intent.ACTION_SEND);
            intent.setType("text/plain");
            File f = new File(Environment.getExternalStorageDirectory().toString() +  "/ScoutData" + "/" + mEvent + "/device" + mDeviceNumber, "data.txt");
            Log.d("Words",Environment.getExternalStorageDirectory().toString() +  "/ScoutData" + "/" + mEvent + "/device" + mDeviceNumber);
            intent.putExtra(Intent.EXTRA_STREAM, Uri.fromFile(f));

            PackageManager pm = getPackageManager();
            List<ResolveInfo> appList = pm.queryIntentActivities(intent, 0);

            if(appList.size() > 0){
                String packageName = null;
                String className = null;
                boolean found = false;
                for (ResolveInfo info: appList){
                    packageName = info.activityInfo.packageName;
                    if (packageName.equals("com.android.bluetooth")){
                        className = info.activityInfo.name;
                        found = true;
                        break;
                    }
                }
                if (!found){
                    Toast.makeText(this, "Bluetooth hasn't been found", Toast.LENGTH_LONG).show();
                }
                else {
                    intent.setClassName(packageName, className);
                    startActivity(intent);
                }
            }
            else{
                Toast.makeText(this, "Bluetooth is not cancelled", Toast.LENGTH_LONG).show();
            }
        }

    }
    private void enableDataTransfer(){
        SendViaBluetooth.setEnabled(true);
    }

    private void diableDataTransfer(){
        SendViaBluetooth.setEnabled(false);
    }

}
