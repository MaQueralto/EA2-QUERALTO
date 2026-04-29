pipeline {
    agent any

    environment {
        IMAGEN = 'nba-stats'
        CONTENEDOR = 'nba-stats-container'
    }

    stages {

        stage('1 - Clonar repositorio') {
            steps {
                echo '📥 Clonando el repositorio desde GitHub...'
                checkout scm
            }
        }

        stage('2 - Construir imagen Docker') {
            steps {
                echo '🐳 Construyendo la imagen Docker...'
                sh 'docker build -t ${IMAGEN} .'
            }
        }

        stage('3 - Ejecutar contenedor') {
            steps {
                echo '🚀 Ejecutando el contenedor...'
                // Usamos echo para simular entrada y ver que el contenedor corre correctamente
                sh 'echo "LeBron James" | docker run -i --rm ${IMAGEN}'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completado exitosamente. Build exitoso.'
        }
        failure {
            echo '❌ El pipeline falló. Revisa los logs arriba.'
        }
    }
}
