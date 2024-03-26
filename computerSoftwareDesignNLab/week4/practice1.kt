package com.example.week4_1

import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.LinearLayout

class MainActivity : AppCompatActivity() {
    lateinit var btnChanger : Button
    lateinit var linLayer : LinearLayout

    var number : Int = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        title = "예제 1"

        /////////////Todo///////////////
        btnChanger = findViewById(R.id.ChangeBtn)
        linLayer = findViewById(R.id.LinLay)

        btnChanger.setOnTouchListener{ view, motionEvent ->
            if(number == 0)
                {
                    linLayer.setBackgroundColor(Color.parseColor("#00FF00"))
                    number += 1
                }
            else if(number == 1)
                {
                    linLayer.setBackgroundColor(Color.parseColor("#0000FF"))
                    number += 1
                }
            else if(number == 2)
                {
                    linLayer.setBackgroundColor(Color.parseColor("#FF0000"))
                    number = 0
                }
                Log.d(number.toString(), "test")
            false
        }
    }
}