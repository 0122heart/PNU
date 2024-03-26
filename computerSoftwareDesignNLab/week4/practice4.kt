package com.example.week4_4

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    lateinit var edit1 : EditText;  lateinit var edit2 : EditText
    lateinit var btnAdd : Button;   lateinit var btnSub : Button
    lateinit var btnMul : Button;   lateinit var btnDiv : Button

    lateinit var textResult : TextView
    lateinit var num1 : String; lateinit var num2 :  String
    var result : Int? = null
    var number : Int = 0
    var tictok : Int = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        title = number.toString() + "회 계산기"

        edit1 = findViewById<EditText>(R.id.Edit1)
        edit2 = findViewById<EditText>(R.id.Edit2)

        btnAdd = findViewById<Button>(R.id.BtnAdd)
        btnSub = findViewById<Button>(R.id.BtnSub)
        btnMul = findViewById<Button>(R.id.BtnMul)
        btnDiv = findViewById<Button>(R.id.BtnDiv)


        textResult = findViewById<TextView>(R.id.TextResult)

        number++

        btnAdd.setOnTouchListener{ view, motionEvent ->
            calculate('+')
            false
        }

        btnSub.setOnTouchListener{ view, motionEvent ->
            calculate('-')
            false
        }

        btnMul.setOnTouchListener{ view, motionEvent ->
            calculate('*')
            false
        }

        btnDiv.setOnTouchListener{ view, motionEvent ->
            calculate('/')
            false
        }
    }

    private fun calculate(operator: Char) {
        val num1Str = edit1.text.toString()
        val num2Str = edit2.text.toString()

        if (num1Str.isEmpty() || num2Str.isEmpty()) {
            textResult.text = "두 개의 숫자를 입력하세요."
            return
        }

        val num1 = num1Str.toInt()
        val num2 = num2Str.toInt()
        var result: Int? = null

        when (operator) {
            '+' -> result = num1 + num2
            '-' -> result = num1 - num2
            '*' -> result = num1 * num2
            '/' -> {
                if (num2 != 0) {
                    result = num1 / num2
                } else {
                    textResult.text = "0으로 나눌 수 없습니다."
                    return
                }
            }
        }

        textResult.text = "계산 결과: $result"
        edit1.setText(result.toString())
        edit2.text.clear()
        edit1.requestFocus()
    }
}