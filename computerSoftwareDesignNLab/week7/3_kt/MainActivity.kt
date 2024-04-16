package com.example.week7_3

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.week7_3.databinding.ActivityMainBinding
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.Channel
import java.time.LocalTime

class MainActivity : AppCompatActivity() {
    private var isRunning = false
    private var isPaused = false
    private var isStop = false
    private lateinit var binding: ActivityMainBinding
    private val channel = Channel<String>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.start.setOnClickListener {
            startStopwatch()
        }

        binding.stop.setOnClickListener {
            stopStopwatch()
        }

        binding.pause.setOnClickListener {
            pauseStopwatch()
        }

        binding.resume.setOnClickListener {
            resumeStopwatch()
        }

        GlobalScope.launch(Dispatchers.Main) {
            for (time in channel) {
                binding.time.text = time
            }
        }
    }

    private fun startStopwatch() {
        if (!isRunning) {
            isRunning = true
            isPaused = false
            isStop = false
            GlobalScope.launch(Dispatchers.Default) {
                var seconds = 0
                while (isRunning) {
                    delay(1000)
                    if (!isPaused && !isStop) {
                        seconds++
                        val formattedTime = formatTime(seconds)
                        withContext(Dispatchers.Main) {
                            binding.time.text = formattedTime
                        }
                    }
                }
            }
        } else {
            Toast.makeText(this, "Stopwatch is already running!", Toast.LENGTH_SHORT).show()
        }
    }

    private fun stopStopwatch() {
        isRunning = false
        isPaused = false
        isStop = true
        channel.close()
        binding.time.text = "00:00:00"
    }

    private fun pauseStopwatch() {
        isPaused = true
    }

    private fun resumeStopwatch() {
        isPaused = false
    }

    private fun formatTime(seconds: Int): String {
        val hour = seconds / 3600
        val minute = (seconds % 3600) / 60
        val second = seconds % 60
        return String.format("%02d:%02d:%02d", hour, minute, second)
    }
}
