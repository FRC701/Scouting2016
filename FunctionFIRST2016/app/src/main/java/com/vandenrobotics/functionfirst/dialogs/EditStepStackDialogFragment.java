package com.vandenrobotics.functionfirst.dialogs;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.support.v4.app.DialogFragment;
import android.app.Dialog;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.CheckBox;
import android.widget.ToggleButton;

import com.vandenrobotics.functionfirst.R;
import com.vandenrobotics.functionfirst.model.StepStack;

/**
 * Created by Programming701-A on 2/25/2014.
 */
public class EditStepStackDialogFragment extends DialogFragment {

    // Use this instance of the interface to deliver action events
    DialogListener mListener;

    public StepStack mStepStack;

    private ToggleButton[] totes = new ToggleButton[6];
    private CheckBox knockedOver;

    // Override the Fragment.onAttach() method to instantiate the NoticeDialogListener
    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);
        // Verify that the host activity implements the callback interface
        try {
            // Instantiate the NoticeDialogListener so we can send events to the host
            mListener = (DialogListener) activity;
        } catch (ClassCastException e) {
            // The activity doesn't implement the interface, throw exception
            throw new ClassCastException(activity.toString()
                    + " must implement DialogListener");
        }
    }




    private void loadStepStack(StepStack stepStack){
        for(int i = 0; i < totes.length; i++){
            totes[i].setChecked(stepStack.mTotes[i]);
        }
        knockedOver.setChecked(stepStack.mKnocked);
    }

    private void saveStepStack(){
        for(int i = 0; i < mStepStack.mTotes.length; i++){
            mStepStack.mTotes[i] = totes[i].isChecked();
        }
        mStepStack.mKnocked = knockedOver.isChecked();
    }
}