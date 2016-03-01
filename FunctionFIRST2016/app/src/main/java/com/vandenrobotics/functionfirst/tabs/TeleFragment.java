package com.vandenrobotics.functionfirst.tabs;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.TextView;

import com.vandenrobotics.functionfirst.views.NumberPicker;

import com.vandenrobotics.functionfirst.R;
import com.vandenrobotics.functionfirst.activities.MatchActivity;
import com.vandenrobotics.functionfirst.model.TeleData;

/**
 * Created by Programming701-A on 12/11/2014.
 */
public class TeleFragment extends Fragment {

    private MatchActivity mActivity;
    private boolean viewsAssigned = false;

    private TeleData mTeleData;

    public TextView lowBar;

    public String LowBar;

    private CheckBox disableDefences;

    private Button B_DamageCounterTele1;
    private Button B_DamageCounterTele2;
    private Button B_DamageCounterTele3;
    private Button B_DamageCounterTele4;

    private NumberPicker P_DamageCounterTele1;
    private NumberPicker P_DamageCounterTele2;
    private NumberPicker P_DamageCounterTele3;
    private NumberPicker P_DamageCounterTele4;
    private NumberPicker P_DamageCounterTele5;

    private NumberPicker BouldersInLowGoal;
    private NumberPicker BouldersInHighGoal;
    private NumberPicker BouldersHighGoalMissed;



    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        View rootView = inflater.inflate(R.layout.fragment_tele, container, false);
        mActivity = (MatchActivity) getActivity();

        mTeleData = mActivity.mMatchData.mTeleData;

        if(!viewsAssigned) assignViews(rootView);
        if(viewsAssigned) loadData(mTeleData);

        return rootView;
    }

    @Override
    public void onViewCreated(View view, Bundle savedInstanceState){
        super.onViewCreated(view, savedInstanceState);
        assignViews(view);
        if(viewsAssigned) loadData(mTeleData);
    }

    @Override
    public void onPause(){
        super.onPause();
        mTeleData = new TeleData(saveData());
        mActivity.mMatchData.mTeleData = mTeleData;
        viewsAssigned=false;
    }

    @Override
    public void onResume(){
        super.onResume();
        assignViews(getView());
        if(viewsAssigned) loadData(mTeleData);
    }

    public void loadData(final TeleData teleData){
        // take the teleData and assign it to each view

        lowBar.setText(LowBar);
        B_DamageCounterTele1.setText(teleData.TeleDefence1);
        B_DamageCounterTele2.setText(teleData.TeleDefence2);
        B_DamageCounterTele3.setText(teleData.TeleDefence3);
        B_DamageCounterTele4.setText(teleData.TeleDefence4);

        P_DamageCounterTele1.setValue(teleData.P_DamageCounterTele1);
        P_DamageCounterTele2.setValue(teleData.P_DamageCounterTele2);
        P_DamageCounterTele3.setValue(teleData.P_DamageCounterTele3);
        P_DamageCounterTele4.setValue(teleData.P_DamageCounterTele4);
        P_DamageCounterTele5.setValue(teleData.P_DamageCounterTele5);

        BouldersInLowGoal.setValue(teleData.BouldersInLowGoal);
        BouldersInHighGoal.setValue(teleData.BouldersInHighGoal);
        BouldersHighGoalMissed.setValue(teleData.BouldersHighGoalMissed);



        if(disableDefences.isChecked())
            disableDefenceViews();
        else
            enableDefenceViews();
    }

    public TeleData saveData(){
        TeleData teleData = new TeleData();

        teleData.LowBar = LowBar;
        teleData.TeleDefence1 = B_DamageCounterTele1.getText().toString();
        teleData.TeleDefence2 = B_DamageCounterTele2.getText().toString();
        teleData.TeleDefence3 = B_DamageCounterTele3.getText().toString();
        teleData.TeleDefence4 = B_DamageCounterTele4.getText().toString();

        teleData.P_DamageCounterTele1 = P_DamageCounterTele1.getValue();
        teleData.P_DamageCounterTele2 = P_DamageCounterTele2.getValue();
        teleData.P_DamageCounterTele3 = P_DamageCounterTele3.getValue();
        teleData.P_DamageCounterTele4 = P_DamageCounterTele4.getValue();
        teleData.P_DamageCounterTele5 = P_DamageCounterTele5.getValue();

        teleData.BouldersInLowGoal = BouldersInLowGoal.getValue();
        teleData.BouldersInHighGoal = BouldersInHighGoal.getValue();
        teleData.BouldersHighGoalMissed = BouldersHighGoalMissed.getValue();


        return teleData;
    }

    private void assignViews(View view){
        try{
            // assign all the custom view info to their respective views in the xml
              lowBar = (TextView)view.findViewById(R.id.text_lowBar);
              B_DamageCounterTele1 = (Button)view.findViewById(R.id.button_damageCounterTele1);
              B_DamageCounterTele2 = (Button)view.findViewById(R.id.button_damageCounterTele2);
              B_DamageCounterTele3 = (Button)view.findViewById(R.id.button_damageCounterTele3);
              B_DamageCounterTele4 = (Button)view.findViewById(R.id.button_damageCounterTele4);

              P_DamageCounterTele1 = (NumberPicker)view.findViewById(R.id.picker_DamageCounterTele1);
              P_DamageCounterTele2 = (NumberPicker)view.findViewById(R.id.picker_DamageCounterTele2);
              P_DamageCounterTele3 = (NumberPicker)view.findViewById(R.id.picker_DamageCounterTele3);
              P_DamageCounterTele4 = (NumberPicker)view.findViewById(R.id.picker_DamageCounterTele4);
              P_DamageCounterTele5 = (NumberPicker)view.findViewById(R.id.picker_DamageCounterTele5);

              BouldersInLowGoal = (NumberPicker)view.findViewById(R.id.picker_bouldersScoredInLowGoal);
              BouldersInHighGoal = (NumberPicker)view.findViewById(R.id.picker_bouldersScoredInHighGoal);
              BouldersHighGoalMissed = (NumberPicker)view.findViewById(R.id.picker_bouldersShotAtHighGoal);

              disableDefences = (CheckBox)view.findViewById(R.id.cb_DisableDefences);

              disableDefences.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v){
                      if(disableDefences.isChecked())
                          disableDefenceViews();
                      else
                          enableDefenceViews();
                  }
            });

              LowBar = lowBar.getText().toString();

              P_DamageCounterTele1.setMinValue(0);
              P_DamageCounterTele1.setMaxValue(2);
              P_DamageCounterTele2.setMinValue(0);
              P_DamageCounterTele2.setMaxValue(2);
              P_DamageCounterTele3.setMinValue(0);
              P_DamageCounterTele3.setMaxValue(2);
              P_DamageCounterTele4.setMinValue(0);
              P_DamageCounterTele4.setMaxValue(2);
              P_DamageCounterTele5.setMinValue(0);
              P_DamageCounterTele5.setMaxValue(2);

              BouldersInLowGoal.setMinValue(0);
              BouldersInLowGoal.setMaxValue(50);
              BouldersInHighGoal.setMinValue(0);
              BouldersInHighGoal.setMaxValue(50);
              BouldersHighGoalMissed.setMinValue(0);


            B_DamageCounterTele1.setTag(0);
            B_DamageCounterTele1.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    B_DamageCounterTele1.setText("Category 1");
                    final int status = (Integer) view.getTag();
                    switch (status) {
                        case 0:
                            B_DamageCounterTele1.setText("Portcullis");
                            view.setTag(1);
                            break;
                        case 1:
                            B_DamageCounterTele1.setText("Cheval de Frise");
                            view.setTag(0);
                            break;/*
                        case 2:
                            B_DamageCounterTele1.setText("Moat");
                            view.setTag(3);
                            break;
                        case 3:
                            B_DamageCounterTele1.setText("Ramparts");
                            view.setTag(4);
                            break;
                        case 4:
                            B_DamageCounterTele1.setText("Drawbridge");
                            view.setTag(5);
                            break;
                        case 5:
                            B_DamageCounterTele1.setText("Sally Port");
                            view.setTag(6);
                            break;
                        case 6:
                            B_DamageCounterTele1.setText("Rock Wall");
                            view.setTag(7);
                            break;
                        case 7:
                            B_DamageCounterTele1.setText("Rough Terrain");
                            view.setTag(0);
                            break;*/
                    }


                }

            });

            B_DamageCounterTele2.setTag(0);
            B_DamageCounterTele2.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    B_DamageCounterTele2.setText("Category 2");
                    final int status = (Integer) view.getTag();
                    switch (status) {
                     /*   case 0:
                            B_DamageCounterTele2.setText("Portcullis");
                            view.setTag(1); //pause
                            break;
                        case 1:
                            B_DamageCounterTele2.setText("Cheval de Frise");
                            view.setTag(2); //pause
                            break;*/
                        case 0:
                            B_DamageCounterTele2.setText("Moat");
                            view.setTag(1);
                            break;
                        case 1:
                            B_DamageCounterTele2.setText("Ramparts");
                            view.setTag(0);
                            break;/*
                        case 4:
                            B_DamageCounterTele2.setText("Drawbridge");
                            view.setTag(5);
                            break;
                        case 5:
                            B_DamageCounterTele2.setText("Sally Port");
                            view.setTag(6);
                            break;
                        case 6:
                            B_DamageCounterTele2.setText("Rock Wall");
                            view.setTag(7);
                            break;
                        case 7:
                            B_DamageCounterTele2.setText("Rough Terrain");
                            view.setTag(0);
                            break;*/
                    }

                }

            });

            B_DamageCounterTele4.setTag(0);
            B_DamageCounterTele4.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    B_DamageCounterTele4.setText("Category 4");
                    final int status = (Integer) view.getTag();
                    switch (status) {
                     /*   case 0:
                            B_DamageCounterTele4.setText("Portcullis");
                            view.setTag(1); //pause
                            break;
                        case 1:
                            B_DamageCounterTele4.setText("Cheval de Frise");
                            view.setTag(2); //pause
                            break;
                        case 2:
                            B_DamageCounterTele4.setText("Moat");
                            view.setTag(3);
                            break;
                        case 3:
                            B_DamageCounterTele4.setText("Ramparts");
                            view.setTag(4);
                            break;
                        case 4:
                            B_DamageCounterTele4.setText("Drawbridge");
                            view.setTag(1);
                            break;
                        case 5:
                            B_DamageCounterTele4.setText("Sally Port");
                            view.setTag(0);
                            break;*/
                        case 0:
                            B_DamageCounterTele4.setText("Rock Wall");
                            view.setTag(1);
                            break;
                        case 1:
                            B_DamageCounterTele4.setText("Rough Terrain");
                            view.setTag(0);
                            break;
                    }
                }

            });

            B_DamageCounterTele3.setTag(0);
            B_DamageCounterTele3.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    B_DamageCounterTele3.setText("Category 3");
                    final int status = (Integer) view.getTag();
                    switch (status) {
                        /*case 0:
                            B_DamageCounterTele3.setText("Portcullis");
                            view.setTag(1); //pause
                            break;
                        case 1:
                            B_DamageCounterTele3.setText("Cheval de Frise");
                            view.setTag(2); //pause
                            break;
                        case 2:
                            B_DamageCounterTele3.setText("Moat");
                            view.setTag(3);
                            break;
                        case 3:
                            B_DamageCounterTele3.setText("Ramparts");
                            view.setTag(4);
                            break;*/
                        case 0:
                            B_DamageCounterTele3.setText("Drawbridge");
                            view.setTag(1);
                            break;
                        case 1:
                            B_DamageCounterTele3.setText("Sally Port");
                            view.setTag(0);
                            break;/*
                        case 6:
                            B_DamageCounterTele3.setText("Rock Wall");
                            view.setTag(7);
                            break;
                        case 7:
                            B_DamageCounterTele3.setText("Rough Terrain");
                            view.setTag(0);
                            break;*/
                    }

                }

            });
            viewsAssigned = true;
        } catch (Exception e) {
            e.printStackTrace();
            viewsAssigned = false;
        }
    }
    private void disableDefenceViews(){
        B_DamageCounterTele1.setEnabled(false);
        B_DamageCounterTele2.setEnabled(false);
        B_DamageCounterTele3.setEnabled(false);
        B_DamageCounterTele4.setEnabled(false);
    }
    private void enableDefenceViews(){
        B_DamageCounterTele1.setEnabled(true);
        B_DamageCounterTele2.setEnabled(true);
        B_DamageCounterTele3.setEnabled(true);
        B_DamageCounterTele4.setEnabled(true);
    }
}
