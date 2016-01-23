package com.vandenrobotics.functionfirst.views;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.vandenrobotics.functionfirst.R;
import com.vandenrobotics.functionfirst.activities.MatchActivity;
import com.vandenrobotics.functionfirst.activities.PitScoutActivity;
import com.vandenrobotics.functionfirst.activities.ScoutActivity;

/**
 * Created by Programming701-A on 1/13/2016.
 */
public class OptionScreen extends Activity {



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.option_screen);

    }

    public void pit_scout(View view){
        Intent intent = new Intent(this, PitScoutActivity.class );
        startActivity(intent);

    }
    public void match_scout(View view){
        Intent intent2 = new Intent(this, ScoutActivity.class);
        startActivity(intent2);
    }

}
