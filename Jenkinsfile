pipeline {
  agent any
  stages {
    stage('checkversion') {
      steps {
          sh 'python3 --version'
          sh 'python3 install sasctl'
      }
    }
     stage('run python') {
      steps {
       
        sh 'python3 ModelPublish.py'
      }
    }

  }
}
