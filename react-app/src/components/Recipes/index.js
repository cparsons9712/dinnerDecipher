import { getRecipes } from "../../store/recipe"
import React, { useState , useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";
import './recipe.css';



function RecipeList() {
    const dispatch = useDispatch();

    useEffect (()=>{
        // trigger the data retrieval from the backend to go into the store
        dispatch(getRecipes())
    }, [dispatch])

    // save the data in the store to a variable we can use.
    const recipes = useSelector((state) => state.recipe)
    const recipeArray = Object.values(recipes)




    return (
    <>
        <h1>Recipes</h1>
        {recipeArray.map((r)=>{
            return (
                <div className="recipeCard">
                    <h2>{r.name}</h2>
                    <div>
                      <p>Cook Time: {r.totalTime} </p>
                      <p>Servings: {r.servings}</p>
                    </div>

                    <p>{r.description}</p>
                    <img src={r.img_url} className="recipeImage" alt={r.name}/>
                    <div className="ingredients">
                        <h3>Ingredients</h3>
                        {Object.values(r.ingredients).map((ing)=>{
                            return <div>{ing.quantity} {ing.unit} {ing.name}</div>
                        })}
                    </div>
                    <div className="instructions">
                        <h3>Directions</h3>
                        <ol>
                            {Object.values(r.directions).map((dir)=>{
                                return <li>{dir.text}</li>
                            })}
                        </ol>
                    </div>
                    <div>
                        {r.source}
                    </div>

                </div>
            )
        })}

    </>



    )
}

export default RecipeList
