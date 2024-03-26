package com.example.myapplication

enum class Food{pizza, burger, chicken}

class Lunch(var menu : Food, var price : Int){
    fun choice_lunch(){
        println("menu : $menu, price : $price")
    }
}

fun main(){
    var lunch: MutableList<Lunch> = mutableListOf()
    lunch.add(Lunch(Food.pizza, 15000))
    lunch.add(Lunch(Food.burger, 7000))
    lunch.add(Lunch(Food.chicken, 25000))

    var myLunch = lunch.filter{it.price < 10000}
    for(lunch: Lunch in myLunch){
        lunch.choice_lunch()
    }
}