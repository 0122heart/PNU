package com.example.week6_1
import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?){
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main) // 레이아웃 XML 파일의 내용을 파싱하여 뷰를 생성하고 속성을 설정합니다.
        val btn: Button = findViewById(R.id.btn_main) // 레이아웃 XML에 있는 버튼의 ID를 통해 버튼 객체를 생성합니다.
        btn.setOnClickListener { // 버튼의 클릭 이벤트를 처리하는 리스너를 설정합니다.
            val intent = Intent(this, SubActivity::class.java) // Intent 객체를 생성하여 새로운 액티비티로 이동할 것을 나타냅니다.
            startActivity(intent) // 생성한 Intent를 사용하여 새로운 액티비티를 시작합니다.
        }
    }
}
