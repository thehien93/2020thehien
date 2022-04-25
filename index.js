var emlpoyees = [
    {name: "quang",age: 20},
    {name: "hien",age: 10},
    {name: "truong",age: 11},
    {name: "khanh",age: 23}
];

// for(var emlpoyee of emlpoyees) {
//     console.log(emlpoyee.name, emlpoyee.age);
// }
 
var myLove = {
    name: "lien",
    age: 20,
    wight: 45
};

for ( var key in myLove) {
    console.log(key,myLove[key]);
}