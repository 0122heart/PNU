package com.example.week7_2.recycler

import android.content.Context
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.example.week7_2.R
import com.example.week7_2.databinding.ItemMainBinding
import com.example.week7_2.model.ItemModel


class MyViewHolder(val binding: ItemMainBinding): RecyclerView.ViewHolder(binding.root)
class MyAdapter(val context: Context, val datas: MutableList<ItemModel>?):
    RecyclerView.Adapter<RecyclerView.ViewHolder>(){

    override fun getItemCount(): Int{return datas?.size ?: 0}

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder
            = MyViewHolder(ItemMainBinding.inflate(LayoutInflater.from(parent.context), parent, false))

    override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
        val binding=(holder as MyViewHolder).binding
        val model=datas!![position]
        binding.itemTitle.text=model.title
        binding.itemDesc.text=model.description
        binding.itemTime.text="${model.author} At ${model.publishedAt}"

        //Glide 활용
        Glide.with(context)
            .load(model.urlToImage) // 여기에서 model.imageUrl는 이미지 URL을 가리키는 ItemModel의 속성이어야 합니다.
//            .placeholder(R.drawable.loading) // 로드 중 표시할 이미지
//            .error(R.drawable.error_image) // 로드 실패 시 표시할 이미지
            .into(binding.itemImage) // itemImage는 ItemMainBinding 내의 ImageView의 ID여야 합니다.
    }
}

