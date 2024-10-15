pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the Git repository
                git branch: 'main', url: 'https://github.com/pvmartins/sample-python-project.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                // Set up a Python virtual environment
                sh '''
                    sudo apt install python3.11-venv
                    python3 -m venv venv
                    source venv/bin/activate
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install the required dependencies from requirements.txt
                sh '''
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                // Run the main Python script (replace with your script name)
                sh '''
                    source venv/bin/activate
                    python main.py
                '''
            }
        }
    }

    post {
        always {
            // Clean up the workspace after the build (optional)
            cleanWs()
        }
        success {
            // Notify the success (can be customized)
            echo 'Build completed successfully!'
        }
        failure {
            // Notify the failure (can be customized)
            echo 'Build failed. Please check the logs.'
        }
    }
}
