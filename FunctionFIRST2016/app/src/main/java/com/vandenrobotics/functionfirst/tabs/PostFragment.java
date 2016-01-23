package com.vandenrobotics.functionfirst.tabs;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.RadioGroup;

import com.vandenrobotics.functionfirst.views.NumberPicker;

import com.vandenrobotics.functionfirst.R;
import com.vandenrobotics.functionfirst.activities.MatchActivity;
import com.vandenrobotics.functionfirst.model.PostData;

/**
 * Created by Programming701-A on 12/11/2014.
 */
public class PostFragment extends Fragment {

    private MatchActivity mActivity;
    private boolean viewsAssigned = false;

    private NumberPicker numFouls;
    private NumberPicker numTechFouls;
    private CheckBox gotRedCard;
    private CheckBox gotYellowCard;
    private CheckBox wasDisabled;
    private CheckBox playedDefensively;
    private CheckBox capture;
    private CheckBox breached;
    private RadioGroup challengeState;
    private RadioGroup scaleState;

    private int challengeStateButtonPressed;
    private int scaleStateButtonPressed;

    private PostData mPostData;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        View rootView = inflater.inflate(R.layout.fragment_post, container, false);
        mActivity = (MatchActivity) getActivity();

        mPostData = mActivity.mMatchData.mPostData;

        if(viewsAssigned) loadData(mPostData);

        return rootView;
    }

    @Override
    public void onViewCreated(View view, Bundle savedInstanceState){
        super.onViewCreated(view, savedInstanceState);
        assignViews(view);
        if(viewsAssigned) loadData(mPostData);
    }

    @Override
    public void onPause(){
        super.onPause();
        mPostData = new PostData(saveData());
        mActivity.mMatchData.mPostData = mPostData;
        viewsAssigned=false;
    }

    @Override
    public void onResume(){
        super.onResume();
        assignViews(getView());
        if(viewsAssigned) loadData(mPostData);
    }

    public void loadData(final PostData postData){
        // take the postData and assign it to each view
        numFouls.setValue(postData.numFouls);
        numTechFouls.setValue(postData.numTechFouls);
        gotRedCard.setChecked(postData.gotRedCard);
        gotYellowCard.setChecked(postData.gotYellowCard);
        wasDisabled.setChecked(postData.wasDisabled);
        playedDefensively.setChecked(postData.playedDefensively);
        capture.setChecked(postData.capture);
        breached.setChecked(postData.breached);
        challengeStateButtonPressed = postData.challengeState;
        scaleStateButtonPressed = postData.scaleState;
    }

    public PostData saveData(){
        PostData postData = new PostData();
        if(viewsAssigned){
            postData.numFouls = numFouls.getValue();
            postData.numTechFouls = numTechFouls.getValue();
            postData.gotRedCard = gotRedCard.isChecked();
            postData.gotYellowCard = gotYellowCard.isChecked();
            postData.wasDisabled = wasDisabled.isChecked();
            postData.playedDefensively = playedDefensively.isChecked();
            postData.capture = capture.isChecked();
            postData.breached = breached.isChecked();
            switch(challengeState.getCheckedRadioButtonId()){
                case R.id.rb_NotAttemptedC:
                    challengeStateButtonPressed = 0;
                    break;
                case R.id.rb_AttemptedC:
                    challengeStateButtonPressed = 1;
                    break;
                case R.id.rb_SuccessfulC:
                    challengeStateButtonPressed = 2;
                    break;
                default:
                    challengeStateButtonPressed = 2;

            }
            postData.challengeState = challengeStateButtonPressed;

            switch(scaleState.getCheckedRadioButtonId()){
                case R.id.rb_NotAttemptedS:
                    scaleStateButtonPressed = 0;
                    break;
                case R.id.rb_AttemptedS:
                    scaleStateButtonPressed = 1;
                    break;
                case R.id.rb_SuccessfulS:
                    scaleStateButtonPressed = 2;
                    break;
                default:
                    scaleStateButtonPressed = 2;
            }
            postData.scaleState = scaleStateButtonPressed;

        }

        return postData;
    }

    private void assignViews(View view){
        try{
            // assign all the custom view info to their respective views in the xml
            numFouls = (NumberPicker)view.findViewById(R.id.pickerNumFouls);
            numTechFouls = (NumberPicker)view.findViewById(R.id.pickerNumTechFouls);
            gotRedCard = (CheckBox)view.findViewById(R.id.cb_gotRedCard);
            gotYellowCard = (CheckBox)view.findViewById(R.id.cb_gotYellowCard);
            wasDisabled = (CheckBox)view.findViewById(R.id.cb_wasDisabled);
            playedDefensively = (CheckBox)view.findViewById(R.id.cb_PlayedDefensively);
            capture = (CheckBox)view.findViewById(R.id.cb_Capture);
            breached = (CheckBox)view.findViewById(R.id.cb_Breached);
            challengeState = (RadioGroup)view.findViewById(R.id.rg_ChallengeState);
            scaleState = (RadioGroup)view.findViewById(R.id.rg_ScaleState);

            switch(challengeStateButtonPressed){
                case 0:
                    challengeState.check(R.id.rb_NotAttemptedC);
                    break;
                case 1:
                    challengeState.check(R.id.rb_AttemptedC);
                    break;
                case 2:
                    challengeState.check(R.id.rb_SuccessfulC);
                    break;
                default:
                    challengeState.check(R.id.rb_NotAttemptedC);
                    break;

            }


            switch(scaleStateButtonPressed){
                case 0:
                    scaleState.check(R.id.rb_NotAttemptedS);
                    break;
                case 1:
                    scaleState.check(R.id.rb_AttemptedS);
                    break;
                case 2:
                    scaleState.check(R.id.rb_SuccessfulS);
                    break;
                default:
                    scaleState.check(R.id.rb_NotAttemptedS);
                    break;

            }

            numFouls.setMinValue(0);
            numFouls.setMaxValue(999);
            numTechFouls.setMinValue(0);
            numTechFouls.setMaxValue(999);

            viewsAssigned = true;
        } catch (Exception e){
            e.printStackTrace();
            viewsAssigned = false;
        }
    }
}
