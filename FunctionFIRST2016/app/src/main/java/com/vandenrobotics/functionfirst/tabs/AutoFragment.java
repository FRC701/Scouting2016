package com.vandenrobotics.functionfirst.tabs;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Adapter;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.CheckBox;

import com.vandenrobotics.functionfirst.dialogs.NoShowDialogFragment;
import com.vandenrobotics.functionfirst.views.NumberPicker;

import android.widget.Spinner;
import android.widget.ToggleButton;

import com.vandenrobotics.functionfirst.R;
import com.vandenrobotics.functionfirst.activities.MatchActivity;
import com.vandenrobotics.functionfirst.model.AutoData;

/**
 * Created by Programming701-A on 12/11/2014.
 */
public class AutoFragment extends Fragment implements AdapterView.OnItemSelectedListener{

    private MatchActivity mActivity;
    private boolean viewsAssigned = false;

    public AutoData mAutoData;

    //private CheckBox noShow;
    private CheckBox hadAuto;
    private CheckBox reachesDefences;
    private CheckBox crossesDefences;
    private Spinner Defences1;
    private Spinner Defences2;
    private ArrayAdapter<CharSequence> DefencesA1;
    private ArrayAdapter<CharSequence> DefencesA2;
    private NumberPicker bouldersInLowGoal;
    private NumberPicker bouldersInHighGoal;
    private CheckBox hadOther;


  //  public NoShowDialogFragment noShowDF;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        View rootView = inflater.inflate(R.layout.fragment_auto, container, false);
        mActivity = (MatchActivity) getActivity();

        mAutoData = mActivity.mMatchData.mAutoData;

        if(viewsAssigned) loadData(mAutoData);

       // noShowDF = new NoShowDialogFragment();

        return rootView;



    }

    @Override
    public void onViewCreated(View view, Bundle savedInstanceState){
        super.onViewCreated(view, savedInstanceState);
        assignViews(view);
        if(viewsAssigned) loadData(mAutoData);
    }

    @Override
    public void onPause(){
        super.onPause();
        mAutoData = new AutoData(saveData());
        mActivity.mMatchData.mAutoData = mAutoData;
        viewsAssigned=false;
    }

    @Override
    public void onResume(){
        super.onResume();
        assignViews(getView());
        if(viewsAssigned) loadData(mAutoData);
    }

    public void loadData(final AutoData autoData){
        // take the autoData and assign it to each view
        hadAuto.setChecked(autoData.hadAuto);
        reachesDefences.setChecked(autoData.reachesDefences);
        crossesDefences.setChecked(autoData.crossesDefences);
        Defences1.setSelection(autoData.Defences1);
        Defences2.setSelection(autoData.Defences2);
        bouldersInLowGoal.setValue(autoData.bouldersInLowGoal);
        bouldersInHighGoal.setValue(autoData.bouldersInHighGoal);
        hadOther.setChecked(autoData.hadOther);

        if(hadAuto.isChecked())
            enableAutoViews();
        else
            disableAutoViews();



    }

    public AutoData saveData(){
        AutoData autoData = new AutoData();
        if(viewsAssigned){
            autoData.hadAuto = hadAuto.isChecked();
            autoData.reachesDefences = reachesDefences.isChecked();
            autoData.crossesDefences = crossesDefences.isChecked();
            autoData.Defences1 =  Defences1.getSelectedItemPosition();
            autoData.Defences2 = Defences2.getSelectedItemPosition();
            autoData.bouldersInLowGoal = bouldersInLowGoal.getValue();
            autoData.bouldersInHighGoal = bouldersInHighGoal.getValue();

            autoData.hadOther = hadOther.isChecked();
        }

        return autoData;
    }

    private void assignViews(View view){
        try{
            // assign all the custom view info to their respective views in the xml
            hadAuto = (CheckBox)view.findViewById(R.id.cb_hadAuto);
            reachesDefences = (CheckBox)view.findViewById(R.id.cb_reachesDefences);
            crossesDefences = (CheckBox)view.findViewById(R.id.cb_crossesDefences);

            Defences1 = (Spinner)view.findViewById(R.id.spinnerDefences1);
            Defences1.setOnItemSelectedListener(this);
            DefencesA1 = ArrayAdapter.createFromResource(mActivity,
                    R.array.DefencesList1, R.layout.spinner_base);
            DefencesA1.setDropDownViewResource(R.layout.spinner_dropdown);
            Defences1.setAdapter(DefencesA1);

            Defences2 = (Spinner)view.findViewById(R.id.spinnerDefences2);
            Defences2.setOnItemSelectedListener(this);
            DefencesA2 = ArrayAdapter.createFromResource(mActivity,
                    R.array.DefencesList1, R.layout.spinner_base);
            DefencesA2.setDropDownViewResource(R.layout.spinner_dropdown);
            Defences2.setAdapter(DefencesA2);

            bouldersInLowGoal = (NumberPicker)view.findViewById(R.id.pickerBouldersInLowGoal);
            bouldersInHighGoal = (NumberPicker)view.findViewById(R.id.pickerBouldersInHighGoal);
            hadOther = (CheckBox) view.findViewById(R.id.cb_hadOther);

            hadAuto.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v){
                    if(hadAuto.isChecked())
                        enableAutoViews();
                    else
                        disableAutoViews();
                }
            });
            crossesDefences.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v){
                    if(crossesDefences.isChecked())
                        enableDefenceViews();
                    else
                        disableDefenceViews();
                }
            });
            reachesDefences.setOnClickListener(new View.OnClickListener(){
                @Override
                public void onClick(View v){
                    if (reachesDefences.isChecked())
                        disableCrossesDefenceViews();
                    else
                        enableCrossesDefencesViews();
                }
            });


            bouldersInLowGoal.setMinValue(0);
            bouldersInLowGoal.setMaxValue(50);
            bouldersInHighGoal.setMinValue(0);
            bouldersInHighGoal.setMaxValue(50);


            viewsAssigned = true;
        } catch (Exception e){
            e.printStackTrace();
            viewsAssigned = false;
        }
    }

    private void enableAutoViews(){
        reachesDefences.setEnabled(true);
        crossesDefences.setEnabled(true);
        bouldersInLowGoal.setEnabled(true);
        bouldersInHighGoal.setEnabled(true);
        /*for(ToggleButton tb : autoStack){
            tb.setEnabled(true);
        } */
        hadOther.setEnabled(true);
    }

    private void disableAutoViews(){
        reachesDefences.setChecked(false);
        reachesDefences.setEnabled(false);
        crossesDefences.setChecked(false);
        crossesDefences.setEnabled(false);
        Defences1.setEnabled(false);
        Defences1.setSelection(0);
        Defences2.setEnabled(false);
        Defences2.setSelection(0);
        bouldersInLowGoal.setValue(0);
        bouldersInLowGoal.setEnabled(false);
        bouldersInHighGoal.setValue(0);
        bouldersInHighGoal.setEnabled(false);
        /*for(ToggleButton tb : autoStack){
            tb.setChecked(false);
            tb.setEnabled(false);
        } */
        hadOther.setChecked(false);
        hadOther.setEnabled(false);
    }
    private void enableDefenceViews(){
        Defences1.setEnabled(true);
        Defences2.setEnabled(true);
        reachesDefences.setEnabled(false);
        reachesDefences.setChecked(false);


    }
    private void disableDefenceViews(){
        Defences1.setEnabled(false);
        Defences1.setSelection(0);
        Defences2.setEnabled(false);
        Defences2.setSelection(0);
        reachesDefences.setEnabled(true);

    }
    private void enableCrossesDefencesViews(){
        crossesDefences.setEnabled(true);
        Defences1.setEnabled(true);
        Defences2.setEnabled(true);
    }

    private void disableCrossesDefenceViews(){
        crossesDefences.setEnabled(false);
        crossesDefences.setChecked(false);
        Defences1.setEnabled(false);
        Defences1.setSelection(0);
        Defences2.setEnabled(false);
        Defences2.setSelection(0);
    }

    public void onItemSelected(AdapterView<?> parent, View view,
                               int pos, long id){

    }

    public void onNothingSelected(AdapterView<?> parent){

    }
}
