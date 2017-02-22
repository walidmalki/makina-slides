# Formation Angular
## Éric Bréhault

--------------------------------------------------------------------------------

# 1 - Présentation générale

--------------------------------------------------------------------------------

# La version 2 ?

AngularJS est la version 1.

À partir de la verison 2, le nom devient "Angular".

La version 4 va paraître prochaînement (mais sera dans la continuité d'Angular 2).

# Presenter Notes

parler du sémantic versionning

--------------------------------------------------------------------------------

# Quel type de framework ?

- Spectre large
- Très structurant
- Fortement contraint

# Presenter Notes

expliquer les différences avec React

--------------------------------------------------------------------------------

# Les grands principes

- Composants
- TypeScript
- build

# Presenter Notes

--------------------------------------------------------------------------------

# 2 - Installation et tooling

# Presenter Notes

--------------------------------------------------------------------------------

# Installation

Installer NodeJS (6.9+) et NPM.

Installer Angular CLI:

    !console
    $ npm install -g @angular/cli

# Presenter Notes

--------------------------------------------------------------------------------

# Le CLI

Permet de générer un projet.

    !console
    $ ng new myproject
    $ cd myproject
    $ ng serve

Fournit des facilités pour le développement.

    !console
    $ ng serve
    
Permet d'y ajouter des composants.

    !console
    $ ng generate component MyComponent

# Presenter Notes

--------------------------------------------------------------------------------

# Installation et premiers pas

- Installer NodeJS et Angular CLI
- Créer un projet
- Le lancer avec `ng serve` et ouvrir http://localhost:4200
- Observer la structure de fichiers générée

[Solution](https://github.com/makinacorpus/angular-training/commit/f865cbf4660be2087da7e6925db7ff931bd833b6)

--------------------------------------------------------------------------------

# 3 - Les concepts

- TypeScript
- Component
- Module
- Injection

--------------------------------------------------------------------------------

# Typescript

- TypeScript superset d'ES6 superset d'ES5
- Un "compilateur" fait la conversion
- Apporte :
    - le typage
    - les classes
    - les décorateurs

--------------------------------------------------------------------------------

# Component

Un composant est une classe avec un décorateur `@Component`.

Il correspond à un tag.

Il a un template HTML, éventuellement des fichiers de style.

--------------------------------------------------------------------------------

# Module

Le module est le point d'entrée de l'app Angular.

Il déclare les composants.

Il charge les modules tiers.

Il définit les injections disponibles.

--------------------------------------------------------------------------------

# Injections

Les composants ont besoin de services globaux (persistence des données, accès au backend, routage, etc.).

Ils les obtiennent par injection de dépendances :
Angular va instancier les services dont on a besoin, et les fournir aux composants.

Les services injectables sont des classes ayant le décorateur `@Injectable`.

Ils sont déclarés dans le module (dans `providers`).

Ils sont fournis aux composants dans leur constructeur.

--------------------------------------------------------------------------------

# 4 - Créer un composant simple

Le CLI permet de générer de nouveaux composants dans l'app.

Nous allons créer un composant pour la page d'accueil :

    !console
    $ ng generate component Home

--------------------------------------------------------------------------------

# Utiliser un composant

Le décorateur `@Component` associe un sélecteur (`selector`) au composant.

C'est sous ce nom qu'on peut utiliser le composant dans nos templates HTML.

Dans le cas présent : 

    !xml
    <app-home></app-home>

[Exemple](https://github.com/makinacorpus/angular-training/commit/3c42e93cf619d0efacc8581db4dbd212a4606902)

--------------------------------------------------------------------------------

# Créer un input

Le décorateur `@Input` permet de déclarer un nouvel attribut pour le composant :

    !javascript
    @Input() message: string;

déclare un attribut `message` qu'on peut utiliser de cette façon :

    !xml
    <app-home message="Bonjour !"></app-home>

[Exemple](https://github.com/makinacorpus/angular-training/commit/75741b6aeb7b9338ebf80cb98ce2e4855ec3259c)

--------------------------------------------------------------------------------

# Lier (i.e. binding) un input à une propriété

Plutôt qu'un message écrit en dur, nous souhaitons passer la valeur d'une propriété du composant `App` :

    !javascript
    welcomeMessage: string = 'Bienvenue ici';

Pour cela, on doit noter l'input entre crochet :

    !xml
    <app-home [message]="welcomeMessage"></app-home>

(sinon le message serait littéralement "welcomeMessage" et non pas "Bienvenue ici")

[Exemple](https://github.com/makinacorpus/angular-training/commit/963495ca67318867b8b8d3ce67f0ccf63805e88e)

--------------------------------------------------------------------------------

# Lier un événement à une méthode

Ajoutons au composant Hom une méthode qui modifie le message :

    !javascript
    changeMessage() {
       this.message = 'This is a new message';
    }

On souhaite appeler cette méthode lorsqu'on clique sur un bouton.
Pour cela, on note l'événement entre parenthèses:

    !xml
    <button (click)="changeMessage()">Change the message</button>

[Exemple](https://github.com/makinacorpus/angular-training/commit/6682d3ace9ad190878db075880e1d0745116c520)

--------------------------------------------------------------------------------

# Input et output

Les **inputs** sont les informations qui sont fournies en entrée au composant.

Ils sont notés entre crochets.

Les **outputs** sont les informations qui sont émises par le composant.

Ils sont notés entre parenthèses.

Pour les éléments pouvant être fournis en entrée et émis en sortie, on peut utiliser les 2 notations ensemble : `[()]`, par exemple pour un champ de formulaire. C'est le two-way data binding. En dehors de l'usage élémentaire pour des formulaires, on préfère l'éviter pour des raisons de performance.

--------------------------------------------------------------------------------

# Syntaxe des templates

Interpolation `{{ }}` : permet d'évaluer une expression.

Par exemple :

    !javascript
    {{ 1 + 2 }} // affiche 2
    {{ message }} // affiche la valeur de la propriété `message` du composant

--------------------------------------------------------------------------------

# Syntaxe des templates

Boucle avec `*ngFor`

Note : les directives structurelles (celles qui utilisent un template propre) sont préfixées par `*`.

Créons une propriété contenant une liste de pokémons et affichons-les dans une liste :

    !xml
    <ul>
      <li *ngFor="let pokemon of pokemons">{{pokemon.name}}</li>
    </ul>

[Exemple](https://github.com/makinacorpus/angular-training/commit/f3f629d4d5781dcaee95c43733e042f527766768)

--------------------------------------------------------------------------------

# Syntaxe des templates

Condition avec `*ngIf` ou `*ngSwitch`

On va créer une méthode qui indique si un pokémon est le plus fort :

    !javascript
    isStronger(pokemon:any) {
        let max_pv = Math.max(...this.pokemons.map(pok => pok.pv));
        return (pokemon.pv == max_pv)
    }

Et on utilise cette méthode dans un `*ngIf` pour afficher une mention à côté du plus fort :

    !xml
    <strong *ngIf="isStronger(pokemon)">Le plus fort !!</strong>

[Exemple](https://github.com/makinacorpus/angular-training/commit/c28624c8128f7fadba7e175958a963717e554e76)

--------------------------------------------------------------------------------

# Syntaxe des templates

Classes (et style) avec `ngClass`  (ou `ngStyle`)

On peut directement lier l'attribut normal `class` :

    !javascript
    private defaultClasses:string = 'btn btn-primary btn-special';

    <div [class]="defaultClasses"></div>

On peut aussi conditionner une classe avec un booléen:

    !xml
    <div [class.alert]="isAlert"></div>

--------------------------------------------------------------------------------

# Syntaxe des templates

Mais la directive `ngClass` est souvent plus simple car elle permet de gérer plusieurs classes dans un dictionnaire :

    !javascript
    getClasses(pokemon:any) {
        return {
            grass: pokemon.type == 'grass',
            electric: pokemon.type == 'electric',
            fire: pokemon.type == 'fire',
            small: pokemon.size < 50,
            medium: pokemon.size < 100 && pokemon.size >= 50,
            big: pokemon.size >= 100
        }
    }

    <li [ngClass]="getClasses(pokemon)">

[Exemple](https://github.com/makinacorpus/angular-training/commit/8431681ebd45a1de742b042259658fc9e32d8e43)

--------------------------------------------------------------------------------

# 5 - Gérer le routage

Le routage permet de naviguer de "pages" en "pages" dans notre application
(en fait, physiquement on reste sur la même page `index.html`).

Le principe est de mettre en correspondance des URLs avec des composants :

    !javascript
    { path: '', component: HomeComponent },
    { path: 'about', component: AboutComponent },

Le composant sera affiché dans un point d'insertion qu'on met généralement dans
le template de l'AppComponent :

    !xml
    <router-outlet></router-outlet>

--------------------------------------------------------------------------------

# Exercice

Créons un composant About et utilisons des routes pour atteindre soit Home soit About.

Solution : [Mettre en place le routage](https://github.com/makinacorpus/angular-training/commit/ad97a817a1e66819c21173bd4217f4d65985f803) [Ajouter About et sa route](https://github.com/makinacorpus/angular-training/commit/6715ca7fc3cd9a463bfc1aeb232d931788391efb)

--------------------------------------------------------------------------------

# Liens vers des routes

On peut très bien faire un lien normal vers une route :

    !html
    <a href="/about">About</a>

Mais cela va recharger la page en entier. [Exemple](https://github.com/makinacorpus/angular-training/commit/21721389b3555f980d472f9f4035a787b6000d36)

Si on veut rendre le routage dynamique, on utilise la directive `routerLink`:

    !xml
    <a routerLink="/about">About</a>

[Exemple](https://github.com/makinacorpus/angular-training/commit/323c37239af8ddc07b51bd68141475a8447c3cc3)

--------------------------------------------------------------------------------

# Routes paramétrées

On peut déclarer des routes contenant des paramètres :

    !javascript
    { path: 'pokemon/:id', component: DetailComponent }

Le module `Router` fournit des services **injectables** (c'est-à-dire appelables depuis n'importe quel composant).
Notamment le service `ActivatedRoute` qui permet d'obtenir des informations sur la route courante.

Le composant cible peut recevoir le (ou les) paramètre(s) d'une route en souscrivant (=subscribe)
à des **Observables** proposés par `ActivatedRoute`.

Dans le cas d'un paramètre, on utilise l'observable `params` :

    !javascript
    this.route.params.subscribe(params => {
        console.log(params['id']);
    }

--------------------------------------------------------------------------------

# Exercice

On va créer [une page de présentation détaillée d'un pokémon](https://github.com/makinacorpus/angular-training/commit/3f74fcb655846f102aa782a693b2cc9f9323a429) et faire [des liens depuis la page d'accueil](https://github.com/makinacorpus/angular-training/commit/5d5ec1c2142722984346e17183cfffa80c6ce8aa).

Note: auparavant on va mettre les données sur les pokémons dans un [fichier de configuration](https://github.com/makinacorpus/angular-training/commit/a82ea22f7a53f08214a7a51411e8e4c2d42aa1f6)

--------------------------------------------------------------------------------

# 6 - Appels au backend

Plutôt que gérer des informations localement, on souhaite utiliser l'API publique http://pokeapi.co/ .

Pour cela on va utiliser le service `http` :

    !javascript
    this.http.get('http://pokeapi.co/api/v2/pokemon/')

Les méthodes (get, post, etc.) de `http` renvoient des observables auquel on souscrit pour obtenir les données.
La méthode `json()` permet de désérialiser les données reçues :

    !javascript
    this.http.get('http://pokeapi.co/api/v2/pokemon/')
    .subscribe(res => {
        this.pokemons = res.json().results
    });

--------------------------------------------------------------------------------

# Exercice

Utiliser http://pokeapi.co/api/v2/pokemon/ pour avoir la liste des Pokémons sur la page d'accueil.
Utiliser http://pokeapi.co/api/v2/pokemon/:id pour avoir les informations d'un pokémon.

[Solution](https://github.com/makinacorpus/angular-training/commit/6376c0b3cb97dca531ef2eaf184aa5b015f44f7f)

L'API est lente, il faut faire un spinner (ou un message de chargement).

[Solution](https://github.com/makinacorpus/angular-training/commit/d7b02efba2cac3d5c6d36b4338677aaef9f7ea10)

--------------------------------------------------------------------------------

# Créer un Injectable

Plutôt qu'appeler `http` directment dans nos composants, il est plus sain de déléguer
tous les appels à un service injectable spécifique.

Pour cela, il faut :

- créer une classe ayant le décorateur `@Injectable`,
- y injecter `http`,
- déclarer le service en tant que `provider` dans le module,
- et injecter notre service dans nos composants.

--------------------------------------------------------------------------------

# Exercice

Créer un service fournissant une méthode `listAll()` et une méthode `get(id)`.

[Solution](https://github.com/makinacorpus/angular-training/commit/9b9462fadb7f03661bf194fce84162b1b6e09809)

--------------------------------------------------------------------------------

# 7 - Gérer des formulaires

# Presenter Notes

--------------------------------------------------------------------------------

# 8 - Tester une app

# Presenter Notes

--------------------------------------------------------------------------------

# 9 - Ajouter des dépendances externes

# Presenter Notes

--------------------------------------------------------------------------------

# 10 - Déployer en prod

# Presenter Notes

build de prod
vhost
Angular Universal

--------------------------------------------------------------------------------