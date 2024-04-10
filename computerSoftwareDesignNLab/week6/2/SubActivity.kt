package com.example.week6_2

import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import android.widget.Toast

class SubActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_sub) // TODO: 새로운 액티비티의 레이아웃 리소스 ID를 설정합니다.

        val data = intent.getStringExtra("data") // 이전 액티비티에서 전달된 데이터를 가져옵니다.
        val btn: Button = findViewById(R.id.btn_sub) // 버튼 객체를 찾습니다.
        val ev = findViewById<EditText>(R.id.ev_sub) // EditText 객체를 찾습니다.
        val res: TextView = findViewById(R.id.res_sub) // 결과를 표시할 TextView 객체를 찾습니다.
        res.text = "$data\n-send from main" // MainActivity로부터 받은 데이터를 TextView에 표시합니다.

        btn.setOnClickListener {
            val newData: String = ev.text.toString() // 새로운 데이터를 EditText에서 가져옵니다.
            if (newData.isBlank()) { // 새로운 데이터가 비어 있는지 확인합니다.
                Toast.makeText(this, "값을 입력 해주세요.", Toast.LENGTH_SHORT).show() // 비어 있다면 토스트 메시지를 출력합니다.
                return@setOnClickListener
            }

            // 새로운 데이터가 비어 있지 않은 경우
            val intent = Intent()
            intent.putExtra("data", newData) // 새로운 데이터를 Intent에 추가합니다.
            setResult(Activity.RESULT_OK, intent) // 결과 코드와 함께 Intent를 설정합니다.
            finish() // 현재 액티비티를 종료합니다.
        }
    }
}
