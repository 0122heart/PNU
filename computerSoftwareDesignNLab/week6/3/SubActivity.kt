package com.example.week6_3

import android.app.Activity
import android.content.Intent
import android.graphics.Bitmap
import android.os.Bundle
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class SubActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_sub)

        val nameAge: TextView = findViewById(R.id.name_age_sub)
        val phone: TextView = findViewById(R.id.phone_sub)
        val address: TextView = findViewById(R.id.address_sub)
        val etc: TextView = findViewById(R.id.etc_sub)
        val image: ImageView = findViewById(R.id.image_sub)
        val btnChange: Button = findViewById(R.id.change_sub)
        val btnReturn: Button = findViewById(R.id.return_sub)

        nameAge.text = intent.getStringExtra("name") + "\n" + intent.getStringExtra("age")
        phone.text = intent.getStringExtra("phone")
        address.text = intent.getStringExtra("address")
        etc.text = intent.getStringExtra("etc")
        val bitmap: Bitmap? = intent.getParcelableExtra("image")
        if (bitmap != null) {
            image.setImageBitmap(bitmap)
        }

        btnReturn.setOnClickListener {
            // Go back to MainActivity
            val intent = Intent()
            setResult(Activity.RESULT_OK, intent)
            finish()
        }

        btnChange.setOnClickListener {
            finish()
        }

    }
}
