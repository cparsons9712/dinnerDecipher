import { getRecipes } from "../../store/recipe"
import React, { useState , useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import './dashboard.css';



function Dashboard() {
    const dispatch = useDispatch();

    const history = useHistory();

    const goToRecipes = () =>{
        history.push('/recipes')
    }

    useEffect (()=>{
        // trigger the data retrieval from the backend to go into the store
        dispatch(getRecipes())
    }, [dispatch])

    // save the data in the store to a variable we can use.
    const recipes = useSelector((state) => state.recipe)
    const recipeArray = Object.values(recipes)




    return (
        <>
        <h2>Dashboard</h2>
        <button onClick={goToRecipes}>See Recipes</button>
        </>
    )
}
export default Dashboard
