package diego.idk;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private Button b;
    private TextView t;
    private int counter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        b = (Button) findViewById(R.id.clickMeButton);
        t = (TextView) findViewById(R.id.textView);

        counter = 1;

    }

    public void clicked(View view){
        t.setText("I was clicked");
        counter++;
    }
}
