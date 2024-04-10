package com.example.week6_2

import android.app.Activity
import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.inputmethod.InputMethodManager
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main) // TODO: 메인 액티비티의 레이아웃 리소스 ID를 설정합니다.
        val btn: Button = findViewById(R.id.btn_main)
        val ev = findViewById<EditText>(R.id.ev_main)
        val res: TextView = findViewById(R.id.res_main)

        btn.setOnClickListener {
            if (ev.text.toString().isBlank()) { // EditText가 비어 있는지 확인합니다.
                Toast.makeText(this, "값을 입력 해주세요.", Toast.LENGTH_SHORT).show()
                return@setOnClickListener // EditText가 비어 있다면 토스트 메시지를 출력하고 종료합니다.
            }
            val data: String = ev.text.toString()
            val intent = Intent(this, SubActivity::class.java)
            intent.putExtra("data", data) // 데이터를 Intent에 추가합니다.
            startActivityForResult(intent, 100) // 결과를 받기 위해 서브 액티비티를 시작합니다.
            ev.setText("") // EditText를 비웁니다.
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        val res: TextView = findViewById(R.id.res_main)
        if (resultCode == Activity.RESULT_OK) {
            when (requestCode) {
                100 -> {
                    res.text = data!!.getStringExtra("data").toString() + "\n-send from sub"
                }
            }
        }
    }
}
